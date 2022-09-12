from django.apps import AppConfig


class DjangosignalsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "djangosignals"
    
    def ready(self):
        import djangosignals.signals