from django.contrib import admin
from .models import IdentityDocument, Message, ReportTicket

admin.site.register(IdentityDocument)
admin.site.register(Message)
admin.site.register(ReportTicket)
