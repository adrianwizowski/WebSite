from django.utils import timezone
from .models import Post
from django.shortcuts import render



def base(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'base/base.html', {'posts': posts})

def base_pl(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'base/base_pl.html', {'posts': posts})