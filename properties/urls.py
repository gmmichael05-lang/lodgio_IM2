from django.urls import path
from . import views
app_name = 'properties'
urlpatterns = [
    path('', views.index, name='index'),
    path('AddNewListing', views.add_listing, name='add_listing'),
    path('AddNewCalendarBlock', views.add_calendar_block, name='add_calendar_block'),
    path('AddNewBooking', views.add_booking, name='add_booking'),
]
