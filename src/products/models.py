from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(default="prod.png", upload_to="products")
    price = models.FloatField(help_text="in KSH")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
