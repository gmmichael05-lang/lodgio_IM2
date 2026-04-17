from django.contrib import admin
from .models import Coupon, CouponUsage, Review

admin.site.register(Review)

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('coupon_id', 'code', 'discount_type', 'discount_value', 'expiration_date', 'is_active')
    list_filter = ('discount_type', 'is_active')
    search_fields = ('code',)

@admin.register(CouponUsage)
class CouponUsageAdmin(admin.ModelAdmin):
    list_display = ('usage_id', 'coupon', 'user', 'booking', 'used_at')
    list_filter = ('used_at',)
    search_fields = ('coupon__code', 'user__username', 'booking__booking_id')
