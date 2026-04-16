from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['listing', 'check_in_date', 'check_out_date', 'total_amount']
        widgets = {
            'listing': forms.Select(attrs={'class': 'form-input'}),
            'check_in_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'check_out_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'total_amount': forms.NumberInput(attrs={'class': 'form-input', 'step': '0.01'}),
        }
