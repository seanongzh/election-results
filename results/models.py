from django.db import models
from elections.models import Election
from candidates.models import Candidate
from parties.models import Party

class Result(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    party = models.ForeignKey(Party, null=True, on_delete=models.SET_NULL)
    votes = models.PositiveIntegerField()
    candidate_is_incumbent = models.BooleanField("incumbent", default=False)
    candidate_is_winner = models.BooleanField("winner", default=False)

    def __str__(self):
        return str(self.election) + ": " + str(self.candidate) + " (" + str(self.votes) + ")"
    
    class Meta:
        ordering = ["election", "-votes"]
