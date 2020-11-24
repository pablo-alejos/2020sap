from django.apps import AppConfig


class UsersapConfig(AppConfig):
    name = 'userSap'
    verbose_name="Usuarios"

    def ready(self):
        import userSap.signals