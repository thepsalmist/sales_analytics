from django.contrib import admin
from .models import Position, Sale, CSV


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = [
        "transaction_id",
        "customer",
        "total_price",
        "salesperson",
        "created_at",
    ]
    list_filter = ["salesperson", "customer"]


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ["product", "quantity", "price"]
    list_filter = ["product"]


@admin.register(CSV)
class CSVAdmin(admin.ModelAdmin):
    list_display = ["file_name", "activated", "created_at"]
