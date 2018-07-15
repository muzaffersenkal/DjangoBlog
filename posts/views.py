from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.


def index(request):
    myObject  = Post.objects.all().first()
    return render(request,'posts/index.html',{'post': myObject})