from django.urls import path
from . import views

urlpatterns = [
    path("hero", views.HeroView.as_view()),
    path("partner", views.PartnerView.as_view()),
    path('test', views.TestView.as_view()),
    path("aboutone", views.AboutOneView.as_view()),
    path("abouttwo", views.AboutTwoView.as_view()),
]

