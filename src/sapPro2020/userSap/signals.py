from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import Account
from userSap.models import UserSap


@receiver(post_save, sender=UserSap)
def create_model_account(sender, instance, created, **kwargs):
    if created:
        instance.account = Account.objects.create()
        instance.save()
