from django.apps import AppConfig
from watson import search as watson

class DataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'data'
    def ready(self):
        Candidate = self.get_model("Candidate")
        ElectedPosition = self.get_model("ElectedPosition")
        Election = self.get_model("Election")
        Party = self.get_model("Party")
        Result = self.get_model("Result")
        watson.register(Candidate)
        watson.register(ElectedPosition)
        watson.register(Election)
        watson.register(Party)
        watson.register(Result)
