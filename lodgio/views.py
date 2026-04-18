from django.shortcuts import render, redirect
from .models import IdentityDocument

def upload_document(request):
    if request.method == "POST":
        IdentityDocument.objects.create(
            user=request.user,
            document_type=request.POST.get('document_type'),
            document_number=request.POST.get('document_number'),
            expiration_date=request.POST.get('expiration_date') or None,
            document_image=request.FILES.get('document_image')
        )
        return redirect('upload_document')

    return render(request, 'identity_document/upload.html')