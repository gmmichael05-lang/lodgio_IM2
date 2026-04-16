from django import forms
from .models import Listing, CalendarBlock


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'address', 'city', 'base_price']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'rows': 4}),
            'address': forms.TextInput(attrs={'class': 'form-input'}),
            'city': forms.TextInput(attrs={'class': 'form-input'}),
            'base_price': forms.NumberInput(attrs={'class': 'form-input', 'step': '0.01'}),
        }


class CalendarBlockForm(forms.ModelForm):
    class Meta:
        model = CalendarBlock
        fields = ['listing', 'start_date', 'end_date', 'reason']
        widgets = {
            'listing': forms.Select(attrs={'class': 'form-input'}),
            'start_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'reason': forms.TextInput(attrs={'class': 'form-input'}),
        }
