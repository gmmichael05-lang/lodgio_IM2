from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model
from django.contrib import messages
import json

from .models import Listing, CalendarBlock, Booking
from .forms import ListingForm, CalendarBlockForm, BookingForm, RegisterForm, EditProfileForm

User = get_user_model()


# ──────────────────────────────────────────────
# LOGIN VIEW
# ──────────────────────────────────────────────
def login_view(request):
    # If already logged in, skip login page
    if 'user_id' in request.session:
        return redirect('properties:home_page')

    msg = ''
    if request.method == 'POST':
        email = request.POST.get('txt_email', '')
        pwd = request.POST.get('txt_password', '')
        user = authenticate(request, email=email, password=pwd)
        if user is not None:
            request.session['user_id'] = user.user_id
            request.session['email'] = user.email
            request.session['full_name'] = user.full_name
            request.session['role'] = user.role
            return redirect('properties:home_page')
        else:
            msg = 'Invalid credentials'

    return render(request, 'properties/login.html', {'msg': msg})


# ──────────────────────────────────────────────
# REGISTER VIEW
# ──────────────────────────────────────────────
def register_view(request):
    if 'user_id' in request.session:
        return redirect('properties:home_page')

    msg = ''
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            full_name = form.cleaned_data['full_name']
            password = form.cleaned_data['password']
            # Create the user with a proper hashed password
            user = User.objects.create_user(
                username=email,  # use email as username too
                email=email,
                password=password,
                full_name=full_name,
            )
            msg = 'Registration successful! Please log in.'
            return render(request, 'properties/login.html', {'msg': msg})
        else:
            # Collect form errors into a single message
            error_messages = []
            for field, errors in form.errors.items():
                for error in errors:
                    error_messages.append(error)
            msg = ' '.join(error_messages)
    else:
        form = RegisterForm()

    return render(request, 'properties/register.html', {'form': form, 'msg': msg})


# ──────────────────────────────────────────────
# HOME PAGE VIEW (session-protected)
# ──────────────────────────────────────────────
def home_page(request):
    if 'user_id' not in request.session:
        return redirect('properties:login')

    listings = Listing.objects.all().order_by('-created_at')
    bookings = Booking.objects.all().order_by('-created_at')
    calendar_blocks = CalendarBlock.objects.all()

    context = {
        'listings': listings,
        'bookings': bookings,
        'calendar_blocks': calendar_blocks,
        'session_user': request.session.get('full_name', request.session.get('email', '')),
    }
    return render(request, 'properties/index.html', context)


# ──────────────────────────────────────────────
# EDIT PROFILE VIEW (session-protected)
# ──────────────────────────────────────────────
def edit_profile(request):
    if 'user_id' not in request.session:
        return redirect('properties:login')

    user = User.objects.get(user_id=request.session['user_id'])

    if request.method == 'POST':
        form = EditProfileForm(request.POST)
        if form.is_valid():
            user.email = form.cleaned_data['email']
            user.full_name = form.cleaned_data['full_name']
            new_password = form.cleaned_data.get('password')
            if new_password:
                user.set_password(new_password)
            user.save()
            # Update session data
            request.session['email'] = user.email
            request.session['full_name'] = user.full_name
            return redirect('properties:home_page')
    else:
        form = EditProfileForm(initial={
            'email': user.email,
            'full_name': user.full_name,
        })

    return render(request, 'properties/edit_profile.html', {'form': form})


# ──────────────────────────────────────────────
# LOGOFF VIEW
# ──────────────────────────────────────────────
def logoff(request):
    request.session.flush()
    return redirect('properties:login')


# ──────────────────────────────────────────────
# ADD LISTING (session-protected)
# ──────────────────────────────────────────────
def add_listing(request):
    if 'user_id' not in request.session:
        return redirect('properties:login')

    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.host = User.objects.get(user_id=request.session['user_id'])
            listing.save()
            messages.success(request, 'Listing added successfully!')
            return redirect('properties:home_page')
    else:
        form = ListingForm()

    return render(request, 'properties/addNewListing.html', {'form': form})


# ──────────────────────────────────────────────
# ADD CALENDAR BLOCK (session-protected)
# ──────────────────────────────────────────────
def add_calendar_block(request):
    if 'user_id' not in request.session:
        return redirect('properties:login')

    if request.method == 'POST':
        form = CalendarBlockForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Calendar block added successfully!')
            return redirect('properties:home_page')
    else:
        form = CalendarBlockForm()

    return render(request, 'properties/addNewCalendarBlock.html', {'form': form})


# ──────────────────────────────────────────────
# ADD BOOKING (session-protected)
# ──────────────────────────────────────────────
def add_booking(request):
    if 'user_id' not in request.session:
        return redirect('properties:login')

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.guest = User.objects.get(user_id=request.session['user_id'])

            # Automatically calculate the total amount
            days_stayed = (booking.check_out_date - booking.check_in_date).days
            if days_stayed < 1:
                days_stayed = 1  # Minimum 1 day charge
            booking.total_amount = booking.listing.base_price * days_stayed

            booking.save()
            messages.success(request, 'Booking added successfully!')
            return redirect('properties:home_page')
    else:
        form = BookingForm()

    listing_prices = {listing.listing_id: float(listing.base_price) for listing in Listing.objects.all()}
    context = {
        'form': form,
        'listing_prices': listing_prices
    }

    return render(request, 'properties/addNewBooking.html', context)
