from django.urls import path
from .views import SignUp, SignIn, Activate,GoogleLogin
# from .views import profile, delete, password
# from users import views as accounts_views

urlpatterns =[
    path('signup', SignUp.as_view()),
    path('signin', SignIn.as_view()),
    path('signin/google', GoogleLogin.as_view()),
    path('activate/<str:uidb64>/<str:token>', Activate.as_view())
#     path('signin/kakao', KakaoLoginCallback),
#     path('home',users.views.home, name = 'home')
#     path('<str:userid>',accounts_views.profile, name = "profile"),
#     path('password',accounts_views.password, name='password'),
#     path('delete', accounts_views.delete, name='delete'),
]