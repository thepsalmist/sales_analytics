from django.contrib import admin
from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ["name", "author", "created_at", "updated_at"]
    list_filter = ["author"]
