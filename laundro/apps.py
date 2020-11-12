from django.apps import AppConfig


class LaundroConfig(AppConfig):
    name = 'laundro'

    def ready(self):
        import laundro.signals.handlers # noqa
