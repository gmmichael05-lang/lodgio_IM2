from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import SearchLog, Wishlist, ListingApproval
from .forms import SearchLogForm, WishlistForm, ListingApprovalForm

@login_required
def index(request):
    search_logs = SearchLog.objects.all().order_by('-searched_at')
    wishlists = Wishlist.objects.all().order_by('-added_at')
    approvals = ListingApproval.objects.all().order_by('-reviewed_at')

    context = {
        'search_logs': search_logs,
        'wishlists': wishlists,
        'approvals': approvals,
    }
    return render(request, 'discovery/index.html', context)

def add_search_log(request):
    if request.method == 'POST':
        form = SearchLogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Search Log added successfully!')
            return redirect('home')
    else:
        form = SearchLogForm()
    return render(request, 'discovery/addNewSearchLog.html', {'form': form})

def add_wishlist(request):
    if request.method == 'POST':
        form = WishlistForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Wishlist item added successfully!')
            return redirect('home')
    else:
        form = WishlistForm()
    return render(request, 'discovery/addNewWishlist.html', {'form': form})

def add_listing_approval(request):
    if request.method == 'POST':
        form = ListingApprovalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Listing Approval added successfully!')
            return redirect('home')
    else:
        form = ListingApprovalForm()
    return render(request, 'discovery/addNewListingApproval.html', {'form': form})
