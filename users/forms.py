from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2'] ###edit this if they want to have their name instead of just their username!!! for ###their profile page
        
        

        
class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email']
        
        
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['first_name', 'last_name', 'image_one', 'image_two', 'image_three','image_four','image_five','image_six','image_seven','image_eight']
        
        

        
    

    
    
                     



