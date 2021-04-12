from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
from django.contrib.auth.models import AnonymousUser
import random
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import pathlib

@login_required    ###makes it so you have to be logged in to your profile to view  might need to edit so that you can view other's profiles
def profile(request): 
    u_form=UserUpdateForm()
    p_form=ProfileUpdateForm()
    
    context={
        'u_form':u_form, 
        'p_form':p_form
    }
    
    return render(request,'users/profile.html')



        
@login_required    
def update_profile(request):
    if request.method=="POST":
        u_form=UserUpdateForm(request.POST, instance=request.user)
        p_form=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Profile has been successfully updated!')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)            
    
    context={
        'u_form':u_form,   ### suggest that users crop their pictures to be approximately square or change the space 
        'p_form':p_form
    }
    
    return render(request,'users/profileupdate.html',context)


    

    
@login_required    ###makes it so you have to be logged in to your profile to view  might need to edit so that you can view other's profiles
def log(request): 
    time_log=[]
    with open(str(pathlib.Path().absolute())+'\\users'+'\\boxes\\'+str(request.user.username)+'\\log.txt', 'r') as file:
        for time in file:
            time_log.append(time)
        time_log.reverse()
    context={
        'times':time_log
    }
    
    return render(request,'users/log.html',context)
        


    
    