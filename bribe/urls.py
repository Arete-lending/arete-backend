from django.urls import path

from . import views

urlpatterns = [
    path("content", views.bribeContent),
    path("action/bribe", views.actionBribe),
]
