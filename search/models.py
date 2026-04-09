from django.db import models

class SearchLog(models.Model):
    user_id = models.IntegerField()
    filters_used = models.TextField()
    searched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Search by user {self.user_id}"