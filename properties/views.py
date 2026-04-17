from django.shortcuts import render, redirect
import json
# from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Listing, CalendarBlock, Booking
from .forms import ListingForm, CalendarBlockForm, BookingForm


# @login_required
def index(request):
    listings = Listing.objects.all().order_by('-created_at')
    bookings = Booking.objects.all().order_by('-created_at')
    calendar_blocks = CalendarBlock.objects.all()

    context = {
        'listings': listings,
        'bookings': bookings,
        'calendar_blocks': calendar_blocks,
    }
    return render(request, 'properties/index.html', context)


from django.contrib.auth import get_user_model

# @login_required
def add_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            User = get_user_model()
            listing.host = User.objects.first()
            listing.save()
            messages.success(request, 'Listing added successfully!')
            return redirect('properties:index')
    else:
        form = ListingForm()

    return render(request, 'properties/addNewListing.html', {'form': form})


# @login_required
def add_calendar_block(request):
    if request.method == 'POST':
        form = CalendarBlockForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Calendar block added successfully!')
            return redirect('properties:index')
    else:
        form = CalendarBlockForm()

    return render(request, 'properties/addNewCalendarBlock.html', {'form': form})


# @login_required
def add_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            User = get_user_model()
            booking.guest = User.objects.first()
            
            # Automatically calculate the total amount
            days_stayed = (booking.check_out_date - booking.check_in_date).days
            if days_stayed < 1:
                days_stayed = 1  # Minimum 1 day charge
            booking.total_amount = booking.listing.base_price * days_stayed
            
            booking.save()
            messages.success(request, 'Booking added successfully!')
            return redirect('properties:index')
    else:
        form = BookingForm()

    listing_prices = {listing.listing_id: float(listing.base_price) for listing in Listing.objects.all()}
    context = {
        'form': form,
        'listing_prices': listing_prices
    }

    return render(request, 'properties/addNewBooking.html', context)
