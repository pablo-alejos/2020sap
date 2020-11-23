from django.apps import AppConfig


class UsersapConfig(AppConfig):
    name = 'userSap'

    def ready(self):
        import userSap.signals