from django.contrib import admin
from .models import Coupon


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('coupon_id', 'code', 'discount_type', 'discount_value', 'expiration_date', 'is_active')
    list_filter = ('discount_type', 'is_active')
    search_fields = ('code',)
