from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = 'account'
    verbose_name="Cuenta"

    def ready(self):
        import account.signals