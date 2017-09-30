"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class locationData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lat = models.TextField(max_length=500,blank=True)
    long = models.TextField(max_length=500,blank=True)
    logDate = models.DateField(null=True, blank=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()