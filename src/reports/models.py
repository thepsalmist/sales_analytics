from django.db import models
from authentication.models import Profile


class Report(models.Model):
    name = models.CharField(max_length=156)
    image = models.ImageField(default="report.png", upload_to="reports")
    remarks = models.TextField(help_text="Your remarks")
    author = models.ForeignKey(Profile, on_delete="models.CASCADE")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
