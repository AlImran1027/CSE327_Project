import importlib

from django.apps import AppConfig


class armsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'armsApp'
from django.apps import AppConfig

class ArmsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'armsApp'

    def ready(self):
        from . import signals