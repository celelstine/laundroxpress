import os
from django.core.exceptions import ValidationError


IMAGE_FILE_TYPES = [
    '.jpg',
    '.jpeg',
    '.png'
]


def validate_image_file_extension(value):
    """
    Validates that a certain file is an image
    """
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = IMAGE_FILE_TYPES
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported image file extension.')
