from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from core.views import LoginView

class CommunicationsLoginView(LoginView):
    pass


@login_required
def add_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)

        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.save()
            messages.success(request, 'Message sent successfully!')
            return redirect('add_message')

    else:
        form = MessageForm()

    return render(request, "communications/addNewMessage.html", {
        "form": form
    })