from django.urls import path
from . import views

urlpatterns = [   path('messages/', views.message_list, name='message_list'),
    path('messages/add/', views.message_add, name='message_add'),
                  ]