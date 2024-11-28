from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
# Create your views here.


def register(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account successfully created!")
            return redirect("homepage_url")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})

def profile(request):
    return render(request, "users/main_profile.html")