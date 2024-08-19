from django.urls import path
from . import views

urlpatterns = [
    path("", views.BlogView.as_view()),
    path("<int:pk>", views.SinglePost.as_view()),
]
