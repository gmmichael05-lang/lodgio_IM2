from django import forms
from .models import SearchLog, Wishlist, ListingApproval

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
