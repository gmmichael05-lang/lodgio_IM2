from django.shortcuts import render, redirect

from identity_document.models import IdentityDocument


def add_identity_document(request):
    if request.method == "POST":
        IdentityDocument.objects.create(
            user=request.user,
            document_type=request.POST.get("document_type"),
            document_number=request.POST.get("document_number"),
            expiration_date=request.POST.get("expiration_date") or None,
            document_image=request.FILES.get("document_image")
        )
        return redirect("add_identity_document")

    return render(request, "identity_document/upload.html")