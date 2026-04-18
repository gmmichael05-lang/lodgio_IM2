from django.db import models
from django.conf import settings


class IdentityDocument(models.Model):
    document_id = models.AutoField(primary_key=True)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    document_type = models.CharField(max_length=50)
    document_number = models.CharField(max_length=100)

    expiration_date = models.DateField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    document_image = models.ImageField(upload_to='documents/')

    def __str__(self):
        return f"{self.document_type} ({self.document_number})"