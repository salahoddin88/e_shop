from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="UserProfile")
    mobile = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        """ String Representation of object"""
        return str(self.user)

    