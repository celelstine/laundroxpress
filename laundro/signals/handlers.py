from django.dispatch import receiver
from django.db.models.signals import post_delete

from laundro.models import (
    Service
)
from utils.general import delete_model_field


@receiver(post_delete, sender=Service)
def delete_service(sender, instance, **kwargs):
    """
    """
    print('came here', instance.image)
    if instance.image:
        delete_model_field(instance.image.name)
