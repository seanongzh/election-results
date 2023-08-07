from django.apps import AppConfig
from watson import search as watson

class CandidatesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'candidates'

    def ready(self):
        Candidate = self.get_model("Candidate")
        watson.register(Candidate)