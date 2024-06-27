from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'

    # For execute in the beging of application
    def ready(self):
        import products.periodic_tasks