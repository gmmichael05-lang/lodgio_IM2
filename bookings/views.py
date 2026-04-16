from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Booking
from .forms import BookingForm


@login_required
def add_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.guest = request.user
            booking.save()
            messages.success(request, 'Booking added successfully!')
            return redirect('listings:index')
    else:
        form = BookingForm()

    return render(request, 'bookings/addNewBooking.html', {'form': form})
