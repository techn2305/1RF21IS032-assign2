# registration/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_customer, name='register_customer'),
    path('products/<str:customer_id>/', views.products, name='products'),
    path('open_savings_account/', views.open_savings_account, name='open_savings_account'),
    path('success/', views.success, name='success'),
]
