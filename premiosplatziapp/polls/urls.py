from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    # Ex: /polls/3
    path("<int:question_id>/detail", views.detail, name="detail"),
    # Ex: /polls/3/results
    path("<int:question_id>/results", views.results, name="results"),
    # Ex: /polls/3/vote
    path("<int:question_id>/vote", views.vote, name="vote"),
]