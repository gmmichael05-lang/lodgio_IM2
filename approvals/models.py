from django.db import models

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

    def __str__(self):
        return f"Approval {self.decision} for listing {self.listing_id}"