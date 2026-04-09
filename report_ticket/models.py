from django.db import models
from django.conf import settings


class ReportTicket(models.Model):
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('Investigating', 'Investigating'),
        ('Resolved', 'Resolved'),
    ]

    report_id = models.AutoField(primary_key=True)
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reports_made', on_delete=models.CASCADE)
    reported_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reports_received', null=True, blank=True,
                                      on_delete=models.SET_NULL)
    reported_listing_id = models.IntegerField(null=True, blank=True)
    reason_text = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Open')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reason_text} - {self.status}"


from django.db import models

# Create your models here.
