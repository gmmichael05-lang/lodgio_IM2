from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'message_id',
        'sender',
        'receiver',
        'content',
        'sent_at'
    )

    search_fields = (
        'content',
        'sender__username',
        'receiver__username'
    )

    list_filter = (
        'sent_at',
    )


from django.contrib import admin

# Register your models here.
