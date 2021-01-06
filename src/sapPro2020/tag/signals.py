from django.db.models.signals import post_save
from django.dispatch import receiver
from userSap.models import Program, Academy
from article.models import Journal
from tag.models import Tag
"""
@receiver(post_save, sender=Program)
def create_model_program(sender, instance, created, **kwargs):
    if created:
        tag = Tag.objects.create()
        tag.name = instance.name
        tag.tag = 'program'
        tag.save()


@receiver(post_save, sender=Academy)
def create_model_academy(sender, instance, created, **kwargs):
    if created:
        tag = Tag.objects.create()
        tag.name = instance.name
        tag.tag = 'academy'
        tag.save()


@receiver(post_save, sender=Journal)
def create_model_journal(sender, instance, created, **kwargs):
    if created:
        tag = Tag.objects.create()
        tag.name = instance.title
        tag.tag = 'journal'
        tag.save()
"""