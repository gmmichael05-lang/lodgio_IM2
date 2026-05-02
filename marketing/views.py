from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import Coupon, CouponUsage, Review
from .forms import CouponForm, CouponUsageForm, ReviewForm


def marketing_login(request):
    """Login page for the marketing module. Uses email as the login field."""
    if request.session.get('marketing_user'):
        return redirect('marketing:index')

    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')

        from accounts.models import User as MarketingUser
        try:
            user_obj = MarketingUser.objects.get(email=email)
            if user_obj.check_password(password):
                user_obj.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user_obj)
                request.session['marketing_user'] = email
                request.session['marketing_user_id'] = user_obj.pk
                messages.success(request, f'Welcome back, {user_obj.username}!')
                return redirect('marketing:index')
            else:
                messages.error(request, 'Invalid credentials.')
        except MarketingUser.DoesNotExist:
            messages.error(request, 'Invalid credentials.')

    return render(request, 'marketing/login.html')



def marketing_logoff(request):
    """Log off and clear the marketing session."""
    request.session.pop('marketing_user', None)
    request.session.pop('marketing_user_id', None)
    logout(request)
    messages.success(request, 'You have been logged off successfully.')
    return redirect('marketing:login')


def edit_profile(request):
    """Edit profile page – session protected."""
    if not request.session.get('marketing_user'):
        messages.warning(request, 'Please log in to access that page.')
        return redirect('marketing:login')

    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name  = request.POST.get('last_name', '').strip()
        email      = request.POST.get('email', '').strip()
        new_password = request.POST.get('new_password', '').strip()
        user = request.user

        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if email:
            user.email = email
            # Update session so login uses the new email
            request.session['marketing_user'] = email
        if new_password:
            user.set_password(new_password)

        user.save()

        # If password changed, re-authenticate so session isn't invalidated
        if new_password:
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            # login() flushes the session, so we need to restore our custom session keys
            request.session['marketing_user'] = user.email
            request.session['marketing_user_id'] = user.pk

        messages.success(request, 'Profile updated successfully!')
        return redirect('marketing:index')

    return render(request, 'marketing/edit_profile.html', {'user': request.user})


def add_new_record(request):
    """Landing page for adding a new record – session protected."""
    if not request.session.get('marketing_user'):
        messages.warning(request, 'Please log in to access that page.')
        return redirect('marketing:login')
    return render(request, 'marketing/add_new_record.html')


def index(request):
    """Home / dashboard – session protected."""
    if not request.session.get('marketing_user'):
        messages.warning(request, 'Please log in to access that page.')
        return redirect('marketing:login')

    coupons = Coupon.objects.all().order_by('-expiration_date')
    usages = CouponUsage.objects.all().order_by('-used_at')
    reviews = Review.objects.all().order_by('-created_at')

    context = {
        'coupons': coupons,
        'usages': usages,
        'reviews': reviews,
    }
    return render(request, 'marketing/index.html', context)


def add_coupon(request):
    if not request.session.get('marketing_user'):
        return redirect('marketing:login')
    if request.method == 'POST':
        form = CouponForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Coupon added successfully!')
            return redirect('marketing:index')
    else:
        form = CouponForm()
    return render(request, 'marketing/addNewCoupon.html', {'form': form})


def add_coupon_usage(request):
    if not request.session.get('marketing_user'):
        return redirect('marketing:login')
    if request.method == 'POST':
        form = CouponUsageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Coupon usage recorded successfully!')
            return redirect('marketing:index')
    else:
        form = CouponUsageForm()
    return render(request, 'marketing/addNewCouponUsage.html', {'form': form})


def add_review(request):
    if not request.session.get('marketing_user'):
        return redirect('marketing:login')
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review added successfully!')
            return redirect('marketing:index')
    else:
        form = ReviewForm()
    return render(request, 'marketing/addNewReview.html', {'form': form})
