from django.contrib import admin
from .models import IdentityDocument
from django.utils.html import format_html


@admin.register(IdentityDocument)
class IdentityDocumentAdmin(admin.ModelAdmin):
    list_display = (
        'document_id',
        'user',
        'document_type',
        'document_number',
        'is_active',
        'uploaded_at',
        'preview_image'
    )

    search_fields = ('document_number', 'document_type', 'user__username')
    list_filter = ('document_type', 'is_active', 'uploaded_at')

    def preview_image(self, obj):
        if obj.document_image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit:cover;border-radius:5px;" />',
                obj.document_image.url
            )
        return "No Image"

    preview_image.short_description = "Preview"