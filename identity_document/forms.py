from django import forms
from .models import IdentityDocument

class IdentityDocumentForm(forms.ModelForm):
    class Meta:
        model = IdentityDocument
        fields = '__all__'