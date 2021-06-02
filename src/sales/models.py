from os import truncate
from django.db import models
from django.utils import timezone
from products.models import Product
from customers.models import Customer
from authentication.models import Profile


class Position(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField(blank=True)
    created_at = models.DateTimeField(blank=True)

    def __str__(self) -> str:
        return f"id {self.id}, product:{self.product.name}, quantity:{self.quantity}"

    def save(self, *args, **kwargs):
        self.price = self.product.price * self.quantity
        return super().save(*args, **kwargs)


class Sale(models.Model):
    transaction_id = models.CharField(max_length=20, blank=True)
    positions = models.ManyToManyField(Position)
    total_price = models.FloatField(blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesperson = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Sales for the amount of Ksh{self.total_price}"

    def save(self, *args, **kwargs):
        if self.transaction_id == "":
            self.transaction_id == ""
        if self.created_at is None:
            self.created_at = timezone.now()
        return super().save(*args, **kwargs)

    @property
    def get_positions(self):
        return self.positions.all()


class CSV(models.Model):
    file_name = models.FileField(upload_to="csvs")
    activated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.file_name)
