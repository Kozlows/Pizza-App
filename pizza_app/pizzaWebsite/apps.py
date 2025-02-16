from django.apps import AppConfig


class PizzawebsiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pizzaWebsite'

    def ready(self):
        import pizzaWebsite.signals