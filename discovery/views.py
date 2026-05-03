from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from .models import SearchLog, Wishlist, ListingApproval
from .forms import SearchLogForm, WishlistForm, ListingApprovalForm, LoginForm, EditProfileForm

class LoginView(View):
    template = "discovery/login.html"
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        form = LoginForm()
        return render(request, self.template, {'form': form})
        
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid email or password.')
                
        return render(request, self.template, {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

@method_decorator(login_required(login_url='login'), name='dispatch')
class EditProfileView(View):
    template_name = 'discovery/edit_profile.html'

    def get(self, request):
        form = EditProfileForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('home')
        return render(request, self.template_name, {'form': form})

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
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
