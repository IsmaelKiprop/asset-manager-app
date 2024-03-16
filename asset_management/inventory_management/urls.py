# asset_management_backend/inventory_management/urls.py

from django.urls import path
from .views import RegisterUser, LoginUser, LogoutUser

urlpatterns = [
    path('auth/register/', RegisterUser.as_view(), name='register'),
    path('auth/login/', LoginUser.as_view(), name='login'),
    path('auth/logout/', LogoutUser.as_view(), name='logout'),
]