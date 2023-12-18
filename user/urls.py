from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("init", views.init),
    path("check", views.isWallet),
]
