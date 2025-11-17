from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('auth/google/', views.GoogleAuthStart.as_view(), name='google-auth-start'),
    path('thank-you/', views.thank_you, name='thank-you'),
]