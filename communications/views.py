from django.shortcuts import render
from django.views import View
from .models import IdentityDocument, Message, ReportTicket

class IndexView(View):
    template_name = 'communications/index.html'
    
    def get(self, request):
        identity_documents = IdentityDocument.objects.all()
        messages = Message.objects.all()
        report_tickets = ReportTicket.objects.all()
        
        return render(request, self.template_name, {
            'identity_documents': identity_documents,
            'messages': messages,
            'report_tickets': report_tickets,
        })
