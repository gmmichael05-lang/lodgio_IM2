from django.contrib import admin
from .models import SearchLog, Wishlist, ListingApproval

admin.site.register(SearchLog)
admin.site.register(Wishlist)
admin.site.register(ListingApproval)
