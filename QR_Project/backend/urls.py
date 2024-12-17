from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from django.urls import path
from backend import views

urlpatterns = [
    path('', views.home, name='home'),  # Root URL
    path('login/', views.user_login, name='login'),  # Login URL
    path('register/', views.register, name='register'),  # Register URL
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard URL
    path('dashboard/', views.dashboard, name='dashboard'),  # Home/Dashboard
    path('view-profile/', views.view_profile, name='view_profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('logout/', LogoutView.as_view(next_page='user_login'), name='logout'),  # Logout
]
