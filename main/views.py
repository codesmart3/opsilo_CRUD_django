from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
import datetime
from django.utils import timezone
from .forms import PostForm
# Create your views here.
def index(request):
    return render(request,'main/index.html')

def blog(request):
    postlist = Post.objects.all()
    return render(request, 'main/blog.html', {'postlist':postlist})

def posting(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'main/posting.html', {'post':post})

def new_post(request):
    if request.method == 'POST':
        if request.POST['mainphoto']:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
                date=timezone.datetime.now(),
            )
        else:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
                date=timezone.datetime.now(),
            )
        return redirect('/blog/')
    return render(request, 'main/new_post.html')

def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/blog/')
    return render(request, 'main/remove_post.html', {'Post': post})

def remove_all(request):
    postlist = Post.objects.all()
    if request.method == 'POST':
        for posts in postlist:
            posts.delete()
        return redirect('/blog/')
    return render(request, 'main/remove_all.html')


def edit_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.postname = request.POST['postname']
        post.contents = request.POST['contents']
        post.mainphoto = request.POST['mainphoto']
        post.date = timezone.datetime.now()
        post.save()
        return redirect('/blog/')
    return render(request, 'main/edit_post.html', {'Post': post})





