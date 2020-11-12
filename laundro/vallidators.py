import os
from django.core.exceptions import ValidationError


IMAGE_FILE_TYPES = [
    '.jpg',
    '.jpeg',
    '.png'
]

VIDEO_FILE_TYPES = [
    '.3g2',
    '.3gp',
    '.avi',
    '.flv',
    '.h264',
    '.m4v',
    '.mkv',
    '.mov',
    '.mp4',
    '.mpg',
    '.mpeg',
    '.rm',
    '.swf',
    '.vob',
    '.wmv',
    '.webm'
]


def validate_image_file_extension(value):
    """
    Validates that a certain file is an image
    """
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = IMAGE_FILE_TYPES
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported image file extension.')


def validate_media_file_extension(value):
    """
    Validates that a certain file is an image or video
    """
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = IMAGE_FILE_TYPES + VIDEO_FILE_TYPES
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported image file extension.')
