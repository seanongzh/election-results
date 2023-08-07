from django.urls import path
from positions.views import PositionDetailView, PositionListView

urlpatterns = [
    path("<slug:slug>", PositionDetailView.as_view(), name="position-detail"),
    path("", PositionListView.as_view(), name="position-list"),
]