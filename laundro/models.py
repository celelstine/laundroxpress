from django.db import models

from utils.model_mixins import BaseAppModelMixin
from laundro.vallidators import validate_image_file_extension
from utils.general import (
    replace_white_space,
    delete_model_field)


def questionset_logo_upload_path(Service, filename):
    """generate upload path for service image"""
    return 'services/{}/image_{}'.format(
        Service.id, replace_white_space(filename))


class Service(BaseAppModelMixin, models.Model):
    """model for services render by laundroxpress"""
    title = models.CharField(unique=True, max_length=60)
    desciption = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to=questionset_logo_upload_path, null=True, blank=True,
        max_length=512, validators=[validate_image_file_extension])

    def save(self, *args, **kwargs):
        # ensure we call clean() on every save
        self.clean()

        old_image_path = None

        if self.pk:
            existing_image_name = Service.objects.get(pk=self.pk).image.name
            if existing_image_name != self.image.name:
                old_image_path = existing_image_name

        # save the object
        super(Service, self).save(*args, **kwargs)

        if old_image_path:
            delete_model_field(old_image_path)
