from django.urls import path
from .views import HomeView, LoginView, logout_view, profile, RegisterView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
]