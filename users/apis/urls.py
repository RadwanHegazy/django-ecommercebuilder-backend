from .views import register, login, profile
from django.urls import path

urlpatterns = [
    path('auth/register/', register.RegisterView.as_view(),name='register'),
    path('auth/login/', login.LoginView.as_view(),name='login'),
    path('profile/', profile.ProfileView.as_view(),name='profile'),
]