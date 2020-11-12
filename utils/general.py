import os
from django.conf import settings


def replace_white_space(text):
    """replace white space with underscore"""
    return ('_').join(text.split(' '))


def delete_model_field(path):
    try:
        os.remove(os.path.join(settings.MEDIA_ROOT, path))
    except Exception as e:
        print('can not delete file', e)
