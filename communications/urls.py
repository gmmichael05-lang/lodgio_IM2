from django.urls import path
from .views import add_message

urlpatterns = [
    path('addNewMessage/', add_message, name='add_message'),
]