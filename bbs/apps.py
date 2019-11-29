from django.apps import AppConfig


class BbsConfig(AppConfig):
    name = 'bbs'

    def ready(self):
        import bbs.signals