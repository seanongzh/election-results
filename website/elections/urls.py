from django.urls import path
from elections.views import ElectionDetailView, ElectionListView

urlpatterns = [
    path("<slug:slug>", ElectionDetailView.as_view(), name="election-detail"),
    path("", ElectionListView.as_view(), name="election-list")
]