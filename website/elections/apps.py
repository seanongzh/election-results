from django.apps import AppConfig
from watson import search as watson

class ElectionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'elections'

    def ready(self):
        Election = self.get_model("Election")
        watson.register(Election)
