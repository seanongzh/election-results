from django.apps import AppConfig
from watson import search as watson

class PositionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'positions'

    def ready(self):
        Position = self.get_model("Position")
        watson.register(Position)