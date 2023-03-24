from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    # Ex: /polls/3
    path("<int:pk>/detail", views.DetailView.as_view(), name="detail"),
    # Ex: /polls/3/results
    path("<int:pk>/results", views.ResultView.as_view(), name="results"),
    # Ex: /polls/3/vote
    path("<int:pk>/vote", views.vote, name="vote"),
]