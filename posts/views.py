from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from .forms import CreatePostForm
from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils.decorators import method_decorator


# Create your views here.


def index(request):
    allPosts  = Post.objects.all()
    return render(request,'posts/index.html',{'posts': allPosts})

def single(request,slug):
    post = get_object_or_404(Post,slug=slug)
    return render(request,'posts/single.html',{'single' : post })


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request,'registration/register.html', {'form':form})



    else:
        form = UserCreationForm()
        return render(request,'registration/register.html',{'form':form})

@login_required(login_url='/login')
def createPost(request):

    if request.method == 'GET':
        form = CreatePostForm()
        return render(request,'posts/create_post.html',{'form':form})

    else:
        form = CreatePostForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/')
        else:
            return render(request,'posts/create_post.html',{'form':form})


@method_decorator(login_required(login_url='/login'),name="dispatch")
class CreatePostView(View):

    form_class = CreatePostForm
    template_name = 'posts/create_post.html'

    def get(self,request,*args,**kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self,request,*args,**kwargs):

        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/')
        else:
            return render(request, self.template_name, {'form': form})


















