from django.db import models
from django.contrib.auth.models import User
# from django import forms
from .utils import get_random_code
from django.template.defaultfilters import slugify
from django.db.models import Q
from PIL import Image
import datetime
from datetime import date
from django.db.models.functions import (ExtractDay, ExtractMonth, ExtractQuarter, ExtractWeek, ExtractWeekDay, ExtractIsoYear, ExtractYear)


###tables messing up https://stackoverflow.com/questions/34548768/django-no-such-table-exception/36453000  VERRYYYY IMPORTANT!!!!!!!!!!
### tables messing up cont. clear the pychaces and then delete the database did the trick but also deletes all the data look at link 
### above for more detailed info

class ProfileManager(models.Manager):    #### maybe using manager to get target audience would increase performance?
    def get_all_profiles(self, me):
        profiles = Profile.objects.all().exclude(user=me)
        return profiles
    def get_all_profiles_to_invite(self, sender):
        profiles = Profile.objects.all().exclude(user = sender)
        profile=Profile.objects.get(user=sender)
        qs = Relationship.objects.filter(Q(sender=profile)|Q(receiver=profile))
        accepted = []
        for rel in qs:
            if rel.status=='accepted':
                accepted.append(rel.receiver)
                accepted.append(rel.sender)
        print(accepted)
        available=[profile for profile in profiles if profile not in accepted]
        print(available)
        return available
        

###profile model does not replace the existing user model but it inherits from it

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE) ### one to one relationship with the user model and delete the profile if the 
        
    
    first_name=models.CharField(max_length=13, blank=True, default='not') #user first name
    last_name=models.CharField(max_length=13, blank=True, default='available') #user last name
    slug=models.SlugField(unique=True, blank=True) #way to uniquely identify each profile
    ##########################################
    ### people who are allowed to access the lock###
    ##########################################
    image_one=models.ImageField(upload_to='gallery_pics',blank=True, null=True, help_text='Note: when updating any of your 8 gallery pictures, it is best to upload approximately square images or the bottom portion of your picture will be automatically cropped out')
    image_two=models.ImageField(upload_to='gallery_pics',blank=True, null=True)
    image_three=models.ImageField(upload_to='gallery_pics',blank=True, null=True)
    image_four=models.ImageField(upload_to='gallery_pics',blank=True, null=True)
    image_five=models.ImageField(upload_to='gallery_pics',blank=True, null=True)
    image_six=models.ImageField(upload_to='gallery_pics',blank=True, null=True)
    image_seven=models.ImageField(upload_to='gallery_pics',blank=True, null=True)
    image_eight=models.ImageField(upload_to='gallery_pics',blank=True, null=True)
    ##########################################
    ### up to 8 people for any given lock###
    ########################################## 
    
    objects=ProfileManager()    
    
### MUST RUN MIGRATIONS AFTER CHANGIN THE MODEL!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def get_friends(self):
        return self.friends.all()
    def get_friends_num(self):
        return self.friends.all().count()
    
    
    
    def save(self, *args,**kwargs):
        if self.slug:
            super().save(*args,**kwargs)
        else:            
            ex= False
            to_slug=slugify(str(self.user)+get_random_code())    ####usernames are unique!!!
            ex=Profile.objects.filter(slug=self.slug).exists()
            while ex:
                to_slug=slugify(to_slug+' ' +str(get_random_code()))
                ex=Profile.objects.filter(slug=to_slug).exists()
            self.slug = to_slug
            super().save(*args,**kwargs)
        
        ####################works pretty well if any problems revert to this########## ###updating shouldnt change the slugs i have in there now

        
            
            
        ######################### saving and cropping the other images ####################
        ######################## resize them so they take up less space ###################
        if self.image_one:
            img_one = Image.open(self.image_one.path)
            width, height = img_one.size  # Get dimensions
            if width > 400 and height > 400:
                img_one.thumbnail((width, height))  # keep ratio but shrink down
            if height < width:
                left = (width - height) / 2
                right = (width + height) / 2
                top = 0
                bottom = height
                img_one = img_one.crop((left, top, right, bottom))
            elif width < height:
                left = 0
                right = width
                top = 0
                bottom = width
                img_one = img_one.crop((left, top, right, bottom))
            if width > 400 and height > 400:
                img_one.thumbnail((400, 400))
                
            img_one.save(self.image_one.path)
            
           ############################################
        if self.image_two:
            img_two = Image.open(self.image_two.path)
            width, height = img_two.size  # Get dimensions
            if width > 400 and height > 400:
                img_two.thumbnail((width, height))  # keep ratio but shrink down
            if height < width:
                left = (width - height) / 2
                right = (width + height) / 2
                top = 0
                bottom = height
                img_two = img_two.crop((left, top, right, bottom))
            elif width < height:
                left = 0
                right = width
                top = 0
                bottom = width
                img_two = img_two.crop((left, top, right, bottom))
            if width > 400 and height > 400:
                img_two.thumbnail((400, 400))

            img_two.save(self.image_two.path)
            #################################
        if self.image_three:
            img_three = Image.open(self.image_three.path)
            width, height = img_three.size  # Get dimensions
            if width > 400 and height > 400:
                img_three.thumbnail((width, height))  # keep ratio but shrink down
            if height < width:
                left = (width - height) / 2
                right = (width + height) / 2
                top = 0
                bottom = height
                img_three = img_three.crop((left, top, right, bottom))
            elif width < height:
                left = 0
                right = width
                top = 0
                bottom = width
                img_three = img_three.crop((left, top, right, bottom))
            if width > 400 and height > 400:
                img_three.thumbnail((400, 400))

            img_three.save(self.image_three.path)
            ###################################
        if self.image_four:
            img_four = Image.open(self.image_four.path)
            width, height = img_four.size  # Get dimensions
            if width > 400 and height > 400:
                img_four.thumbnail((width, height))  # keep ratio but shrink down
            if height < width:
                left = (width - height) / 2
                right = (width + height) / 2
                top = 0
                bottom = height
                img_four = img_four.crop((left, top, right, bottom))
            elif width < height:
                left = 0
                right = width
                top = 0
                bottom = width
                img_four = img_four.crop((left, top, right, bottom))
            if width > 400 and height > 400:
                img_four.thumbnail((400, 400))

            img_four.save(self.image_four.path)
            #####################################
        if self.image_five:
            img_five = Image.open(self.image_five.path)
            width, height = img_five.size  # Get dimensions
            if width > 400 and height > 400:
                img_five.thumbnail((width, height))  # keep ratio but shrink down
            if height < width:
                left = (width - height) / 2
                right = (width + height) / 2
                top = 0
                bottom = height
                img_five = img_five.crop((left, top, right, bottom))
            elif width < height:
                left = 0
                right = width
                top = 0
                bottom = width
                img_five = img_five.crop((left, top, right, bottom))
            if width > 400 and height > 400:
                img_five.thumbnail((400, 400))

            img_five.save(self.image_five.path)
            ####################################
        if self.image_six:
            img_six = Image.open(self.image_six.path)
            width, height = img_six.size  # Get dimensions
            if width > 400 and height > 400:
                img_six.thumbnail((width, height))  # keep ratio but shrink down
            if height < width:
                left = (width - height) / 2
                right = (width + height) / 2
                top = 0
                bottom = height
                img_six = img_six.crop((left, top, right, bottom))
            elif width < height:
                left = 0
                right = width
                top = 0
                bottom = width
                img_six = img_six.crop((left, top, right, bottom))
            if width > 400 and height > 400:
                img_six.thumbnail((400, 400))

            img_six.save(self.image_six.path)
            ##################################
        if self.image_seven:
            img_seven = Image.open(self.image_seven.path)
            width, height = img_seven.size  # Get dimensions
            if width > 400 and height > 400:
                img_seven.thumbnail((width, height))  # keep ratio but shrink down
            if height < width:
                left = (width - height) / 2
                right = (width + height) / 2
                top = 0
                bottom = height
                img_seven = img_seven.crop((left, top, right, bottom))
            elif width < height:
                left = 0
                right = width
                top = 0
                bottom = width
                img_seven = img_seven.crop((left, top, right, bottom))
            if width > 400 and height > 400:
                img_seven.thumbnail((400, 400))

            img_seven.save(self.image_seven.path)
            ######################################
        if self.image_eight:
            img_eight = Image.open(self.image_eight.path)
            width, height = img_eight.size  # Get dimensions
            if width > 400 and height > 400:
                img_eight.thumbnail((width, height))  # keep ratio but shrink down
            if height < width:
                left = (width - height) / 2
                right = (width + height) / 2
                top = 0
                bottom = height
                img_eight = img_eight.crop((left, top, right, bottom))
            elif width < height:
                left = 0
                right = width
                top = 0
                bottom = width
                img_eight = img_eight.crop((left, top, right, bottom))
            if width > 400 and height > 400:
                img_eight.thumbnail((400, 400))

            img_eight.save(self.image_eight.path)
                    
        ###################################################################################
        
            
    
    

        

    