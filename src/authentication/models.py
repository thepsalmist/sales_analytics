from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    User profiles model
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="No Bio")
    avatar = models.ImageField(default="prof.png", upload_to="profiles")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user.username} profile"
