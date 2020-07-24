from django.urls import path
from .views import SignUp, SignIn

urlpatterns =[
    path('signin', SignIn.as_view()),
    path('signup', SignUp.as_view())
]
