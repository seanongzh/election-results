from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from parties.models import Party
from results.models import Result
from candidates.models import Candidate

class PartyDetailView(DetailView):
    model = Party

    def get_context_data(self, **kwargs):
        object = super().get_object()
        context = super().get_context_data(**kwargs)
        context["candidates"] = Candidate.objects.filter(id__in=Result.objects.filter(party=object).values_list("candidate", flat=True))
        context["model"] = "Party"
        return context

class PartyListView(ListView):
    model = Party

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model"] = "Parties"
        return context