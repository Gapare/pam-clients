from django.contrib import admin
from django.urls import path, include
from auth_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', include('auth_app.urls')),  
    path('auth/', include('social_django.urls', namespace='social')),
    path('auth/success/', views.auth_success, name='auth-success'),
    path('thank-you/', views.auth_success, name='thank-you'),
]