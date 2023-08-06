from django.urls import path
from parties.views import PartyDetailView, PartyListView

urlpatterns = [
    path("<slug:slug>", PartyDetailView.as_view(), name="party-detail"),
    path("", PartyListView.as_view(), name="party-list"),
]