from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import Account
from author.models import Author

@receiver(post_save, sender=Account)
def create_update_model_author(sender, instance, created, **kwargs):
    if created:
        author = Author.objects.create()
        instance.author_info = author
        author.save()
        instance.save()
    else:
        author = Author.objects.get(id=instance.author_info.id)
        author.firstName = instance.firstName
        author.lastNameA = instance.lastNameA
        author.lastNameB =instance.lastNameB
        author.save()


