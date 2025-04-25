from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Flights

@receiver(post_save, sender=Flights)
def notify_users(sender, instance, **kwargs):
    print(f"Flight {instance.name} has been updated.")
