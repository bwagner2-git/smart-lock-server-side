from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
import face_recognition as fr
import pathlib

@receiver(post_save, sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        
@receiver(post_save, sender=User) #every time a profile is updated it is saved and we save all of the encondings of the faces in text files
def save_profile(sender,instance,**kwargs):
    instance.profile.save()
    
    
    if instance.profile.image_one:
        target=instance.profile.image_one.url
        pic=fr.load_image_file(str(pathlib.Path().absolute())+target)
        encoding = fr.face_encodings(pic)[0]
        #self.user.username
        with open(str(pathlib.Path().absolute())+'\\users'+'\\boxes\\'+instance.username+'\\people\\one.txt', 'w') as file:
            for value in encoding:
                file.write('%s\n' % value) 
    else:
        with open(str(pathlib.Path().absolute())+'\\users'+'\\boxes\\'+instance.username+'\\people\\one.txt', 'w') as file:
            file.write('') # if the person removes a person from the allowed people then get rid of their encoding
    
    
    if instance.profile.image_two:
        target=instance.profile.image_two.url
        pic=fr.load_image_file(str(pathlib.Path().absolute())+target)
        encoding = fr.face_encodings(pic)[0]
        #self.user.username
        with open(str(pathlib.Path().absolute())+'\\users'+'\\boxes\\'+instance.username+'\\people\\two.txt', 'w') as file:
            for value in encoding:
                file.write('%s\n' % value) 
    else:
        with open(str(pathlib.Path().absolute())+'\\users'+'\\boxes\\'+instance.username+'\\people\\two.txt', 'w') as file:
            file.write('')
            
            
       
    if instance.profile.image_three:
        target=instance.profile.image_three.url
        pic=fr.load_image_file(str(pathlib.Path().absolute())+target)
        encoding = fr.face_encodings(pic)[0]
        #self.user.username
        with open(str(pathlib.Path().absolute())+'\\users'+'\\boxes\\'+instance.username+'\\people\\three.txt', 'w') as file:
            for value in encoding:
                file.write('%s\n' % value) 
    else:
        with open(str(pathlib.Path().absolute())+'\\users'+'\\boxes\\'+instance.username+'\\people\\three.txt', 'w') as file:
            file.write('')
     
    
    if instance.profile.image_four:
        target=instance.profile.image_four.url
        pic=fr.load_image_file(str(pathlib.Path().absolute())+target)
        encoding = fr.face_encodings(pic)[0]
        #self.user.username
        with open(str(pathlib.Path().absolute())+'\\users'+'\\boxes\\'+instance.username+'\\people\\four.txt', 'w') as file:
            for value in encoding:
                file.write('%s\n' % value) 
    else:
        with open(str(pathlib.Path().absolute())+'\\users'+'\\boxes\\'+instance.username+'\\people\\four.txt', 'w') as file:
            file.write('')
    
    
    if instance.profile.image_five:
        target=instance.profile.image_five.url
        pic=fr.load_image_file(str(pathlib.Path().absolute())+target)
        encoding = fr.face_encodings(pic)[0]
        #self.user.username
        with open(str(pathlib.Path().absolute())+'\\users'+'\\boxes\\'+instance.username+'\\people\\five.txt', 'w') as file:
            for value in encoding:
                file.write('%s\n' % value) 
    else:
        with open(str(pathlib.Path().absolute())+'\\users'+'\\boxes\\'+instance.username+'\\people\\five.txt', 'w') as file:
            file.write('')
    
    
    
    if instance.profile.image_six:
        target=instance.profile.image_six.url
        pic=fr.load_image_file(str(pathlib.Path().absolute())+target)
        encoding = fr.face_encodings(pic)[0]
        #self.user.username
        with open(str(pathlib.Path().absolute())+'\\users'+'\\boxes\\'+instance.username+'\\people\\six.txt', 'w') as file:
            for value in encoding:
                file.write('%s\n' % value) 
    else:
        with open(str(pathlib.Path().absolute())+'\\users'+'\\boxes\\'+instance.username+'\\people\\six.txt', 'w') as file:
            file.write('')
    
    
    if instance.profile.image_seven:
        target=instance.profile.image_seven.url
        pic=fr.load_image_file(str(pathlib.Path().absolute())+target)
        encoding = fr.face_encodings(pic)[0]
        #self.user.username
        with open(str(pathlib.Path().absolute())+'\\users'+'\\boxes\\'+instance.username+'\\people\\seven.txt', 'w') as file:
            for value in encoding:
                file.write('%s\n' % value) 
    else:
        with open(str(pathlib.Path().absolute())+'\\users'+'\\boxes\\'+instance.username+'\\people\\seven.txt', 'w') as file:
            file.write('')

     
    if instance.profile.image_eight:
        target=instance.profile.image_eight.url
        pic=fr.load_image_file(str(pathlib.Path().absolute())+target)
        encoding = fr.face_encodings(pic)[0]
        #self.user.username
        with open(str(pathlib.Path().absolute())+'\\users'+'\\boxes\\'+instance.username+'\\people\\eight.txt', 'w') as file:
            for value in encoding:
                file.write('%s\n' % value) 
    else:
        with open(str(pathlib.Path().absolute())+'\\users'+'\\boxes\\'+instance.username+'\\people\\eight.txt', 'w') as file:
            file.write('')    
        
        
        
        
        
        
        
        
        

    