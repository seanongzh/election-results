from django.shortcuts import get_object_or_404, render
from data.models import Candidate, Election, Party, ElectedPosition

def home(request):
    return render(request, "data/base.html")

def candidate(request, candidate_id):
    candidate = get_object_or_404(Candidate, pk=candidate_id)
    return render(request, "data/base_candidate.html", {'candidate': candidate})

def election(request, election_id):
    election = get_object_or_404(Election, pk=election_id)
    return render(request, "data/base_election.html", {'election': election})

def party(request, party_id):
    party = get_object_or_404(Party, pk=party_id)
    return render(request, "data/base_party.html", {'party': party})

def position(request, position_id):
    position = get_object_or_404(ElectedPosition, pk=position_id)
    return render(request, "data/base_position.html", {'position': position})