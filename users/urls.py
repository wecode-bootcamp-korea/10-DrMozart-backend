from django.urls import path
from .views import SignUp, SignIn, Activate,GoogleLogin

urlpatterns =[
    path('signup', SignUp.as_view()),
    path('signin', SignIn.as_view()),
    path('signin/google', GoogleLogin.as_view()),
    path('activate/<str:uidb64>/<str:token>', Activate.as_view())
]