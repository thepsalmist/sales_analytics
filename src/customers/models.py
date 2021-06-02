from django.db import models


class Customer(models.Model):
    """
    A customers Model
    """

    name = models.CharField(max_length=256)
    logo = models.ImageField(default="logo.png", upload_to="customers")

    def __str__(self) -> str:
        return self.name
