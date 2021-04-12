from django.urls import path
from . import views    ### check and see if this is right   from . imports from current directory
from users import views as user_views


urlpatterns = [
    path('', views.home, name = 'blog-home'),
]
