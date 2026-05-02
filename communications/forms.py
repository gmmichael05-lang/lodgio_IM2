from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'content']
        widgets = {
            'receiver': forms.Select(attrs={
                'class': 'form-input'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-input',
                'rows': 4,
                'placeholder': 'Write your message here...'
            }),
        }