from django.shortcuts import get_object_or_404, render
from data.models import Candidate

def home(request):
    return render(request, "data/base.html")

def candidate(request, candidate_id):
    candidate = get_object_or_404(Candidate, pk=candidate_id)
    return render(request, "data/base_candidate.html", {'candidate': candidate})