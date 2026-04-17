from django.shortcuts import render
from django.views import View
from .models import SearchLog, Wishlist, ListingApproval

class IndexView(View):
    template_name = 'discovery/index.html'
    
    def get(self, request):
        searches = SearchLog.objects.all()
        wishlists = Wishlist.objects.all()
        approvals = ListingApproval.objects.all()
        
        return render(request, self.template_name, {
            'searches': searches,
            'wishlists': wishlists,
            'approvals': approvals,
        })
