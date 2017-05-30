from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from .models import ProfileStatus


@receiver(post_save, sender=User)
def create_profilestatus(created, instance, **kwargs):
    """ Create a userprofile for every new user """
    if created:
        ProfileStatus.objects.create(owner=instance)