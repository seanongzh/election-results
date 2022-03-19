from django.urls import path
from data import views

app_name = "data"
urlpatterns = [
    path("", views.home, name="home"),
    path("candidate/<int:candidate_id>", views.candidate, name="candidate-detail"),
]