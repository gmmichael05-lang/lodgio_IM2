from django.db import models
from django.conf import settings

class Listing(models.Model):
    class Status(models.TextChoices):
        PENDING = 'Pending', 'Pending'
        ACTIVE = 'Active', 'Active'
        REJECTED = 'Rejected', 'Rejected'
        SUSPENDED = 'Suspended', 'Suspended'

    listing_id = models.AutoField(primary_key=True)
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='listings')
    title = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    approved_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_listings')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'listing'

    def __str__(self):
        return self.title

class CalendarBlock(models.Model):
    block_id = models.AutoField(primary_key=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='calendar_blocks')
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'calendar_block'

    def __str__(self):
        return f"{self.listing.title} blocked from {self.start_date} to {self.end_date}"

class Booking(models.Model):
    class Status(models.TextChoices):
        PENDING = 'Pending', 'Pending'
        CONFIRMED = 'Confirmed', 'Confirmed'
        COMPLETED = 'Completed', 'Completed'

    booking_id = models.AutoField(primary_key=True)
    guest = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bookings')
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'booking'

    def __str__(self):
        return f"Booking {self.booking_id} - at {self.listing}"
