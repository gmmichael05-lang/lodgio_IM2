from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_id', 'guest', 'listing', 'rating', 'created_at')
    list_filter = ('rating',)
    search_fields = ('guest__email', 'listing__title', 'comment')
    ordering = ('-created_at',)
