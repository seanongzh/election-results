from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from positions.models import Position
from elections.models import Election

class PositionDetailView(DetailView):
    model = Position

    def get_context_data(self, **kwargs):
        object = super().get_object()
        context = super().get_context_data(**kwargs)
        context["elections"] = Election.objects.filter(position=object)
        context["model"] = "Position"
        return context
    
class PositionListView(ListView):
    model = Position

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model"] = "Positions"
        return context