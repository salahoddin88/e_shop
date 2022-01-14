from django.dispatch import receiver
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


# Signals 
""" When User model is created or save create_profile, save_profile will receive a signal  """
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        print('create_profile signal ')
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    print('updated...', instance)
