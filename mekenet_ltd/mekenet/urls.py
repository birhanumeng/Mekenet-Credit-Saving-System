from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('customers/', views.customers, name='customers'),
    path('customer/', views.customers, name='customer'),
    path('saves/', views.saving, name='saves'),
    path('loans/', views.loans, name='loans'),
    path('create_saving/', views.createSaving, name='create_saving'),
    path('update_saving/<str:key>/', views.updateSaving, name='update_saving'),
    path('delete_saving/<str:key>/', views.deleteSaving, name='delete_saving'),
    path('create_loan/', views.createLoan, name='create_loan'),
]