from django.apps import AppConfig


class CarpartsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'carparts'

    def ready(self):
        from .signals import create_profile, save_profile
