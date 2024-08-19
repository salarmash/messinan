from django.urls import path
from . import views

urlpatterns = [
    path("header", views.HeaderView.as_view()),
    path("", views.ServiceView.as_view()),
    path("<int:pk>", views.SingleService.as_view()),
]
