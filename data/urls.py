from django.urls import path
from data import views

app_name = "data"
urlpatterns = [
    path("", views.home, name="home"),
    path("candidate/<int:candidate_id>", views.candidate, name="candidate-detail"),
    path("election/<int:election_id>", views.election, name="election-detail"),
    path("party/<int:party_id>", views.party, name="party-detail"),
    path("position/<int:position_id>", views.position, name="position-detail")
]