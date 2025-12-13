from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import SignUpForm, UpdateUserForm, UpdateProfileForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "You have successfully registered and logged in!:)")
            return redirect("accounts:profile")
    else:
        form = SignUpForm()
    return render(request, "accounts/signup.html", {"form" : form})

@login_required
def profile(request):
    # Витягуємо профіль и юзера
    profile_object, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, instance=profile_object)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile is update successfully!")
            return redirect("accounts:profile")
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=profile_object)

    return render(request, "accounts/profile.html", {"user_form" : user_form, "profile_form" : profile_form})

def custom_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "You successfully login :)")
            return redirect("accounts:profile")
    else:
        form = AuthenticationForm(request)
    return render(request, "accounts/login.html", {"form" : form})

@login_required
def logout_profile(request):
    logout(request)
    return redirect("accounts:custom_login")