from django.shortcuts import render
from django.http import HttpResponse
# from .models import post, sponsored_post
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def mission(request):
    return render(request, 'blog/mission.html')

# Create your views here.
