from django.shortcuts import render
from .models import ListingApproval

def approval_list(request):
    approvals = ListingApproval.objects.all()
    return render(request, 'approvals/approval_list.html', {'approvals': approvals})