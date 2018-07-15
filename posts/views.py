from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post


# Create your views here.


def index(request):
    allPosts  = Post.objects.all()
    return render(request,'posts/index.html',{'posts': allPosts})

def single(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    return render(request,'posts/single.html',{'single' : post })
