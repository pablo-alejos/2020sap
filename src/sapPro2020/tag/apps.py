from django.apps import AppConfig


class TagConfig(AppConfig):
    name = 'tag'
    verbose_name = 'Etiqueta'
    
    def ready(self):
        import tag.signals