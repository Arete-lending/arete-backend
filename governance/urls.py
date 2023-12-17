from django.urls import path

from . import views

urlpatterns = [
    path("header", views.ATEHeader),
    path("vesting", views.listVesting),
    path("action/forge", views.actionForge),
    path("action/extract", views.actionExtract),
]
