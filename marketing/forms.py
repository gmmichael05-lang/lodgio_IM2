from django import forms
from .models import Coupon, CouponUsage, Review


class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = ['code', 'discount_type', 'discount_value', 'expiration_date', 'is_active']
        widgets = {
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
            'discount_value': forms.NumberInput(attrs={'step': '0.01'}),
        }


class CouponUsageForm(forms.ModelForm):
    class Meta:
        model = CouponUsage
        fields = ['coupon', 'user', 'booking']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['booking', 'guest', 'listing', 'rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4}),
            'rating': forms.NumberInput(attrs={'step': '0.1', 'min': '1.0', 'max': '5.0'}),
        }
