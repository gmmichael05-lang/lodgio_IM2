from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from listings.models import Listing
from bookings.models import Booking


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

    def __str__(self):
        return f"Review {self.review_id} – {self.listing} ({self.rating}/5)"
