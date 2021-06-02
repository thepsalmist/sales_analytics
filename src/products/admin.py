from django.contrib import admin
from django.db import models
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "created_at", "updated_at"]
    list_filter = ["created_at"]
    search_fields = ["name"]
