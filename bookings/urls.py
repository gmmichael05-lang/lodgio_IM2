from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('addNewBooking', views.add_booking, name='add_booking'),
]
