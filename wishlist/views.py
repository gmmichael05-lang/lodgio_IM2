from django.shortcuts import render
from .models import Wishlist

def wishlist_list(request):
    wishlists = Wishlist.objects.all()
    return render(request, 'wishlist/wishlist_list.html', {'wishlists': wishlists})