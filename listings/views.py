from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Listing, CalendarBlock
from .forms import ListingForm, CalendarBlockForm
from bookings.models import Booking


@login_required
def index(request):
    listings = Listing.objects.all().order_by('-created_at')
    bookings = Booking.objects.all().order_by('-created_at')
    calendar_blocks = CalendarBlock.objects.all()

    context = {
        'listings': listings,
        'bookings': bookings,
        'calendar_blocks': calendar_blocks,
    }
    return render(request, 'listings/index.html', context)


@login_required
def add_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.host = request.user
            listing.save()
            messages.success(request, 'Listing added successfully!')
            return redirect('listings:index')
    else:
        form = ListingForm()

    return render(request, 'listings/addNewListing.html', {'form': form})


@login_required
def add_calendar_block(request):
    if request.method == 'POST':
        form = CalendarBlockForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Calendar block added successfully!')
            return redirect('listings:index')
    else:
        form = CalendarBlockForm()

    return render(request, 'listings/addNewCalendarBlock.html', {'form': form})
