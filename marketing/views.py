from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Coupon, CouponUsage, Review
from .forms import CouponForm, CouponUsageForm, ReviewForm


# @login_required
def index(request):
    coupons = Coupon.objects.all().order_by('-expiration_date')
    usages = CouponUsage.objects.all().order_by('-used_at')
    reviews = Review.objects.all().order_by('-created_at')

    context = {
        'coupons': coupons,
        'usages': usages,
        'reviews': reviews,
    }
    return render(request, 'marketing/index.html', context)


# @login_required
def add_coupon(request):
    if request.method == 'POST':
        form = CouponForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Coupon added successfully!')
            return redirect('marketing:index')
    else:
        form = CouponForm()

    return render(request, 'marketing/addNewCoupon.html', {'form': form})


# @login_required
def add_coupon_usage(request):
    if request.method == 'POST':
        form = CouponUsageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Coupon usage recorded successfully!')
            return redirect('marketing:index')
    else:
        form = CouponUsageForm()

    return render(request, 'marketing/addNewCouponUsage.html', {'form': form})


# @login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review added successfully!')
            return redirect('marketing:index')
    else:
        form = ReviewForm()

    return render(request, 'marketing/addNewReview.html', {'form': form})
