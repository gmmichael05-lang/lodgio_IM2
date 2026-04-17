from django.shortcuts import render
from django.views import View
from .models import Coupon, CouponUsage, Review

class IndexView(View):
    template_name = 'marketing/index.html'
    
    def get(self, request):
        coupons = Coupon.objects.all()
        usages = CouponUsage.objects.all()
        reviews = Review.objects.all()
        
        return render(request, self.template_name, {
            'coupons': coupons,
            'usages': usages,
            'reviews': reviews,
        })
