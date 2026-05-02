from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-input'
        }),
        required=True
    )
    
    class Meta:
        model = User
        fields = ['full_name', 'username', 'email']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Full Name'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'Email'
            }),
        }
class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email',
            'class': 'form-input'
        }),
        required=True
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-input'
        }),
        required=True
    )

class ProfileForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-input",
            "placeholder": "New Password (leave blank to keep current)"
        }),
        required=False
    )

    class Meta:
        model = User
        fields = ["full_name", "username", "first_name", "last_name", "email"]

        widgets = {
            "full_name": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Full Name"
            }),
            "username": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Username"
            }),
            "first_name": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "First Name"
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Last Name"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-input",
                "placeholder": "Email"
            }),
        }