from django.apps import AppConfig
from watson import search as watson

class ResultsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'results'

    def ready(self):
        Result = self.get_model("Result")
        # watson.register(Result)