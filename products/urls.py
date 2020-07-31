from django.urls import path

from . import views

urlpatterns = [
    path("main", views.ProductMainView.as_view()),
    path("all", views.ProductAllView.as_view()),
    path("detail/<int:pk>", views.ProductDetailView.as_view()),
]
