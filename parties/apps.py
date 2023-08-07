from django.apps import AppConfig
from watson import search as watson

class PartiesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'parties'

    def ready(self):
        Party = self.get_model("Party")
        watson.register(Party)
