from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProjectView.as_view()),
    path("<int:pk>", views.Single.as_view())
]
