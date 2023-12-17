from django.urls import path

from . import views

urlpatterns = [
    path("header", views.voteHeader),
    path("content", views.voteContent),
    path("action/vote", views.actionVote),
]
