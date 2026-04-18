from django.shortcuts import render, redirect
from .forms import MessageForm

def add_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.save()
            return redirect('add_message')
    else:
        form = MessageForm()

    return render(request, "communications/addNewMessage.html", {
        "form": form
    })