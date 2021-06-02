from django.contrib import admin
from django.db import models
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(models.ModelAdmin):
    list_display = ["name"]
