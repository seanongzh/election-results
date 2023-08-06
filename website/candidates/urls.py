from django.urls import path
from candidates.views import CandidateDetailView, CandidateListView

urlpatterns = [
    path("<slug:slug>", CandidateDetailView.as_view(), name="candidate-detail"),
    path("", CandidateListView.as_view(), name="candidate-list"),
]