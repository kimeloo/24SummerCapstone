from django.apps import AppConfig


class AdminPageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'admin_page'

    # def ready(self):
        # import admin_page.signals