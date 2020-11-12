from django.db import models
from django.conf import settings

from utils.model_mixins import BaseAppModelMixin
from laundro.vallidators import (
    validate_image_file_extension,
    validate_media_file_extension)
from utils.general import (
    replace_white_space,
    delete_model_field)


def get_service_image_upload_path(service, filename):
    """generate upload path for service image"""
    return 'services/{}/image_{}'.format(
        service.id, replace_white_space(service.title))


class Service(BaseAppModelMixin, models.Model):
    """model for services render by laundroxpress"""
    title = models.CharField(unique=True, max_length=60)
    desciption = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to=get_service_image_upload_path, null=True, blank=True,
        max_length=512, validators=[validate_image_file_extension])
    price_range = models.CharField(null=True, blank=True, max_length=50)

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


def get_product_image_upload_path(product, filename):
    """generate upload path for product image"""
    return 'services/{}/products/{}'.format(
        product.service_id, replace_white_space(product.title))


class Product(BaseAppModelMixin, models.Model):
    """model for products in laundroxpress"""
    title = models.CharField(unique=True, max_length=80)
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name='products')
    price = models.FloatField()
    image = models.ImageField(
        upload_to=get_service_image_upload_path, null=True, blank=True,
        max_length=512, validators=[validate_image_file_extension])
    desciption = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # ensure we call clean() on every save
        self.clean()

        old_image_path = None

        if self.pk:
            existing_image_name = Product.objects.get(pk=self.pk).image.name
            if existing_image_name != self.image.name:
                old_image_path = existing_image_name

        # save the object
        super(Product, self).save(*args, **kwargs)

        if old_image_path:
            delete_model_field(old_image_path)


class Order(BaseAppModelMixin, models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name='orders')
    total_cost = models.FloatField()
    outstanding = models.FloatField()

    RECIEVED = 'rcv'
    IN_PROGRESS = 'inp'
    COMPLETED = 'com'
    FULFILLED = 'ful'

    STATUS_CHOICES = (
        (RECIEVED, 'Recieved'),
        (IN_PROGRESS, 'In Progress'),
        (COMPLETED, 'Completed'),
        (FULFILLED, 'Fulfilles')
    )
    status = models.CharField(
        choices=STATUS_CHOICES, max_length=3, default=RECIEVED)


class OrderItem(BaseAppModelMixin, models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='orderitems')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='orderitems')

    RECIEVED = 'rcv'
    IN_PROGRESS = 'inp'
    COMPLETED = 'com'
    FULFILLED = 'ful'

    STATUS_CHOICES = (
        (RECIEVED, 'Recieved'),
        (IN_PROGRESS, 'In Progress'),
        (COMPLETED, 'Completed'),
        (FULFILLED, 'Fulfilles')
    )
    status = models.CharField(
        choices=STATUS_CHOICES, max_length=3, default=RECIEVED)
    cost = models.FloatField()
    amount = models.PositiveIntegerField(default=1)
    total_cost = models.FloatField()


def get_gallery_media_upload_path(gallery, filename):
    """generate upload path for gallery image"""
    return 'gallery/{}/{}'.format(
        gallery.content_type, replace_white_space(gallery.title))


class Gallery(BaseAppModelMixin, models.Model):
    """multimedia for display"""
    title = models.CharField(unique=True, max_length=80)

    IMAGE = 'img'
    VIDEO = 'vid'

    CONTENT_TYPE_CHOICES = (
        (IMAGE, 'Image'),
        (VIDEO, 'Video')
    )
    content_type = models.CharField(
        choices=CONTENT_TYPE_CHOICES, max_length=3)

    media = models.ImageField(
        upload_to=get_gallery_media_upload_path, null=True, blank=True,
        max_length=512, validators=[validate_media_file_extension])
