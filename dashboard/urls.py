from django.urls import path

from . import views

urlpatterns = [
    path("header", views.dashboardHeader),
    path("header/supply", views.headerSupply),
    path("header/borrow", views.headerBorrow),
    path("supply", views.supply),
    path("borrow", views.borrow),
    path("asset/supply", views.assetsToSupply),
    path("asset/borrow", views.assetsToBorrow),
    path("action/supply", views.actionSupply),
    path("action/borrow", views.actionBorrow),
    path("action/withdraw", views.actionWithdraw),
    path("action/repay", views.actionRepay),
]
