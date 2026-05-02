from django.urls import path
from . import views

app_name = 'properties'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('homepage/', views.home_page, name='home_page'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('logoff/', views.logoff, name='logoff'),
    path('AddNewListing', views.add_listing, name='add_listing'),
    path('AddNewCalendarBlock', views.add_calendar_block, name='add_calendar_block'),
    path('AddNewBooking', views.add_booking, name='add_booking'),
]
