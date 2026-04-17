from django.db import models


class SearchLog(models.Model):
    user_id = models.IntegerField()
    filters_used = models.TextField()
    searched_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'search_log'

    def __str__(self):
        return f"Search by user {self.user_id}"


class Wishlist(models.Model):
    user_id = models.IntegerField()
    listing_id = models.IntegerField()
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'wishlist'

    def __str__(self):
        return f"Wishlist item for user {self.user_id}"


class ListingApproval(models.Model):
    DECISION_CHOICES = [
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    listing_id = models.IntegerField()
    admin_id = models.IntegerField()
    decision = models.CharField(max_length=10, choices=DECISION_CHOICES)
    reviewed_at = models.DateTimeField(auto_now_add=True)
    remarks = models.TextField(blank=True)

    class Meta:
        db_table = 'listing_approval'

    def __str__(self):
        return f"Approval {self.decision} for listing {self.listing_id}"
