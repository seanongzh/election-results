from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from candidates.models import Candidate
from results.models import Result

class CandidateDetailView(DetailView):
    model = Candidate

    def get_context_data(self, **kwargs):
        object = super().get_object()
        context = super().get_context_data(**kwargs)
        context["results"] = Result.objects.filter(candidate=object)
        context["model"] = "Candidate"
        return context

class CandidateListView(ListView):
    model = Candidate

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model"] = "Candidates"
        return context