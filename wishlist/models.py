from django.db import models

class Wishlist(models.Model):
    user_id = models.IntegerField()
    listing_id = models.IntegerField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Wishlist item for user {self.user_id}"