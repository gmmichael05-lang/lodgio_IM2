from django.urls import path
from .views import add_message, CommunicationsLoginView

urlpatterns = [
    path('addNewMessage/', add_message, name='add_message'),
    path('login/', CommunicationsLoginView.as_view(), name='communications_login'),
]