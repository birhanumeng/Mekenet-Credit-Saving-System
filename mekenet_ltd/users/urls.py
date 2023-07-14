from django.urls import path
from . import views


urlpatterns = [
    path('', views.searchProfile, name='search_profile'),
    path('user_profile/', views.userProfile, name='user_profile'),
    path('user_register/', views.userRegister, name='user_register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]