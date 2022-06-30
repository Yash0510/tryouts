from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from . import views
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_nested import routers


urlpatterns = [
    path('signup', views.SignUp.as_view()),
    path('login', views.Login.as_view(), name='token_obtain_pair'),
    path('login/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
]
