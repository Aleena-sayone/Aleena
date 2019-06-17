from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ProfileForm
from . import signals

#from .import view

# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserRegisterForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)
        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            try:
                user = user_form.save()
                #user.set_password(user.password)
                user.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.image = request.FILES['image'] #name of field
                profile.save()
                # Update our variable to tell the template registration was successful.
                registered = True
            except:
                return HttpResponseRedirect('../login')
            messages.success(request, f'Your Account has been created! You are now able to Log In !')
            return HttpResponseRedirect('../login')
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserRegisterForm()
        profile_form = ProfileForm()

    # Render the template depending on the context.
    return render(request,'register/register.html',{'user_form': user_form, 'profile_form': profile_form, 'registered': registered},)
# #*********************************************************


# @login_required
# def settings(request):
#     user = request.user

#     try:
#         google_login = user.social_auth.get(provider='Google')
#     except UserSocialAuth.DoesNotExist:
#         google_login = None

#     can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

#     return render(request, '../login.html', {
        
#         'google_login': google_login,
#         'can_disconnect': can_disconnect
#     })


# #*********************************************************
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance= request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance= request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been updated !')
            return HttpResponseRedirect('../profile')
    else:
        u_form = UserUpdateForm(instance= request.user)
        p_form = ProfileUpdateForm(instance= request.user.profile)
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request,'register/profile.html', context)

