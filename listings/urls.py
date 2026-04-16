from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    path('', views.index, name='index'),
    path('addNewListing', views.add_listing, name='add_listing'),
    path('addNewCalendarBlock', views.add_calendar_block, name='add_calendar_block'),
]
