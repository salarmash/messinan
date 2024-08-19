from django.urls import path
from . import views

urlpatterns = [
    path("", views.AboutView.as_view()),
    path("counter", views.CounterView.as_view()),
    path("award", views.AwardView.as_view()),
]
