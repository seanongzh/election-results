from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from elections.models import Election
from results.models import Result

class ElectionDetailView(DetailView):
    model = Election

    def get_context_data(self, **kwargs):
        object = super().get_object()
        context = super().get_context_data(**kwargs)
        context["results"] = Result.objects.filter(election=object)
        context["model"] = "Election"
        return context
    
class ElectionListView(ListView):
    model = Election

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model"] = "Elections"
        return context