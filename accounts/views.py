from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic.base import View
from .forms import LoginForm

class HomeView(View):
    template_name = "accounts/index.html"
    
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return render(request, self.template_name)

class LoginView(View):
    template = 'accounts/login.html'
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('accounts:index')
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
                return redirect('accounts:index')
            else:
                messages.error(request, 'Invalid email or password.')
                
        return render(request, self.template, {'form': form})
