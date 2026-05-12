from django.apps import AppConfig

# from .models import ProfileModel
class UsermanagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usermanager'

    def ready(self):
        import usermanager.signals