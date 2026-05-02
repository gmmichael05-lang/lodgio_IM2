from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from .forms import LoginForm, EditProfileForm

@method_decorator(login_required(login_url='/'), name='dispatch')
class HomeView(View):
    template_name = "accounts/index.html"
    
    def get(self, request):
        return render(request, self.template_name)

class LoginView(View):
    template = 'accounts/login.html'
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        form = LoginForm()
        return render(request, self.template, {'form': form})
        
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid email or password.')
                
        return render(request, self.template, {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')

@method_decorator(login_required(login_url='/'), name='dispatch')
class EditProfileView(View):
    template_name = 'accounts/edit_profile.html'

    def get(self, request):
        form = EditProfileForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('home')
        return render(request, self.template_name, {'form': form})
