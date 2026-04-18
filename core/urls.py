from django.urls import path
from .views import HomeView, LoginView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
]