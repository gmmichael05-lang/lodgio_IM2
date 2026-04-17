from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from properties.models import Listing, Booking


class Coupon(models.Model):
    class DiscountType(models.TextChoices):
        PERCENTAGE = 'Percentage', 'Percentage'

    coupon_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50, unique=True)
    discount_type = models.CharField(
        max_length=20,
        choices=DiscountType.choices,
        default=DiscountType.PERCENTAGE
    )
    discount_value = models.DecimalField(max_digits=5, decimal_places=2)
    expiration_date = models.DateField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'coupon'

    def __str__(self):
        return f"{self.code} ({self.discount_value}%)"


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

    class Meta:
        db_table = 'coupon_usage'

    def __str__(self):
        return f"Usage {self.usage_id} – {self.coupon.code} by {self.user}"


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    booking = models.ForeignKey(
        Booking, on_delete=models.CASCADE, related_name='reviews'
    )
    guest = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews'
    )
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name='reviews'
    )
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[MinValueValidator(1.0), MaxValueValidator(5.0)]
    )
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'review'

    def __str__(self):
        return f"Review {self.review_id} – {self.listing} ({self.rating}/5)"
