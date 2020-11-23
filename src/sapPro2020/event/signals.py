from django.db.models.signals import post_save
from django.dispatch import receiver
from event.models import Forum
from event.models import Symposium
from event.models import Congress
from event.models import Event

@receiver(post_save, sender=Forum)
def create_model_forum(sender, instance, created, **kwargs):
    if created:
        print("Creating event...")
        event = Event.objects.create()
        event.name = instance.name
        event.event = 'forum'
        event.save()

@receiver(post_save, sender=Symposium)
def create_model_symposium(sender, instance, created, **kwargs):
    if created:
        print("Creating event...")
        event = Event.objects.create()
        event.name = instance.name
        event.event = 'symposium'
        event.save()
        
@receiver(post_save, sender=Congress)
def create_model_congress(sender, instance, created, **kwargs):
    if created:
        print("Creating event...")
        event = Event.objects.create()
        event.name = instance.name
        event.event = 'congress'
        event.save()