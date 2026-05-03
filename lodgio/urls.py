"""
URL configuration for lodgio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from discovery import views as discovery_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', discovery_views.LoginView.as_view(), name='login'),
    path('home/', discovery_views.index, name='home'),
    path('edit-profile/', discovery_views.EditProfileView.as_view(), name='edit_profile'),
    path('logout/', discovery_views.LogoutView.as_view(), name='logout'),
    path('searchlog/', discovery_views.add_search_log, name='add_search_log'),
    path('wishlist/', discovery_views.add_wishlist, name='add_wishlist'),
    path('listing-approval/', discovery_views.add_listing_approval, name='add_listing_approval'),
    path('Properties/', include('properties.urls')),
    path('accounts/', include('accounts.urls')),
    path('finances/', include('finances.urls')),
    path('communications/', include('communications.urls')),
    path('marketing/', include('marketing.urls')),
]
