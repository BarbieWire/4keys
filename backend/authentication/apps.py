from django.apps import AppConfig

class CustomAuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'
    
    def ready(self):
        import authentication.signals.change_password 
        import authentication.signals.user_created
