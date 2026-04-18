from django.urls import path
from . import views

app_name = 'discovery'

urlpatterns = [
    path('', views.index, name='index'),
    path('AddNewSearchLog', views.add_search_log, name='add_search_log'),
    path('AddNewWishlist', views.add_wishlist, name='add_wishlist'),
    path('AddNewListingApproval', views.add_listing_approval, name='add_listing_approval'),
]
