from django.urls import path
from . import views

urlpatterns = [
    path('', views.finance_home, name='finance_home'),
    path('add/', views.add_transaction, name='add_transaction'),
]
