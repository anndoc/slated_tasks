from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import RegisteredUser


@receiver(post_save, sender=get_user_model())
def create_registered_user(sender, instance, created, **kwargs):
    """
    Create RegisteredUser instance
    """
    if created:
        RegisteredUser.objects.create(user=instance)
