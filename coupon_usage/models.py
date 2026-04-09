from django.db import models
from django.conf import settings
from coupon.models import Coupon
from bookings.models import Booking


class CouponUsage(models.Model):
    usage_id = models.AutoField(primary_key=True)
    coupon = models.ForeignKey(
        Coupon, on_delete=models.CASCADE, related_name='usages'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='coupon_usages'
    )
    booking = models.ForeignKey(
        Booking, on_delete=models.CASCADE, related_name='coupon_usages',
        null=True, blank=True
    )
    used_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Usage {self.usage_id} – {self.coupon.code} by {self.user}"
