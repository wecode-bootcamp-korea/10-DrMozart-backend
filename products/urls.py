from django.urls import path

from . import views

urlpatterns = [
    path("main", views.MainView.as_view()),
    path("all", views.AllView.as_view()),
]
