from django.shortcuts import render
from django.utils import timezone
from .models import Post # Comment, Reaction
from django.contrib.auth.models import User


def post_list(request):
    suser = User.objects.get(username='SuperU')
    posts = Post.objects.filter(author=suser).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
