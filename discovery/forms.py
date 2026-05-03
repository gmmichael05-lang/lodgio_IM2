from django import forms
from django.contrib.auth import get_user_model
from .models import SearchLog, Wishlist, ListingApproval

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['full_name', 'email', 'phone_number']

class SearchLogForm(forms.ModelForm):
    class Meta:
        model = SearchLog
        fields = ['user_id', 'filters_used']
        widgets = {
            'filters_used': forms.Textarea(attrs={'rows': 3}),
        }

class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['user_id', 'listing_id']

class ListingApprovalForm(forms.ModelForm):
    class Meta:
        model = ListingApproval
        fields = ['listing_id', 'admin_id', 'decision', 'remarks']
        widgets = {
            'remarks': forms.Textarea(attrs={'rows': 3}),
        }
