from django.contrib import admin
from .models import CouponUsage


@admin.register(CouponUsage)
class CouponUsageAdmin(admin.ModelAdmin):
    list_display = ('usage_id', 'coupon', 'user', 'booking', 'used_at')
    list_filter = ('coupon',)
    search_fields = ('user__email', 'coupon__code')
    ordering = ('-used_at',)
