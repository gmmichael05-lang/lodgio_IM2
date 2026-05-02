from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib import messages

from .forms import LoginForm, RegistrationForm, ProfileForm

class HomeView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('core:login')
        return render(request, "core/index.html")

class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('core:index')
        return render(request, "core/register.html", {"form": RegistrationForm()})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Registration successful! Please login.')
            return redirect('core:login')
        return render(request, "core/register.html", {"form": form})
class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('core:index')
        return render(request, "core/login.html", {"form": LoginForm()})

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

            if user:
                login(request, user)
                request.session['session_message'] = 'Login successful! Welcome back.'
                return redirect('core:index')
            else:
                messages.error(request, "Invalid email or password")

        return render(request, "core/login.html", {"form": form})
def logout_view(request):
    logout(request)
    return redirect('core:login')
@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            if password:
                user.set_password(password)
                update_session_auth_hash(request, user)
            user.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('core:profile')
    else:
        form = ProfileForm(instance=request.user)
        
    return render(request, "core/profile.html", {"form": form})