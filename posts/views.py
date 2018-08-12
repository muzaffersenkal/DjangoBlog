from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from .forms import CreatePostForm
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import TemplateView,RedirectView,ListView,DetailView,CreateView,DeleteView
from django.utils.decorators import method_decorator





# Class Based Views


class IndexView(TemplateView):
    template_name = 'posts/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        context['posts']  = Post.objects.all()
        context['title'] = 'Son Yazılar'
        return context

class HomeRedirectView(RedirectView):

    pattern_name = 'index'

    def get_redirect_url(self, *args, **kwargs):
        return super(HomeRedirectView,self).get_redirect_url(*args,**kwargs)


class BlogView(ListView):
    template_name = "posts/blog.html"
    model = Post
    context_object_name = "blogPost"
    paginate_by = 3
    #queryset = Post.objects.filter(title__icontains='django')

    #def get_queryset(self):
        #burada işlemleri yapabilirsiniz.
      #  return Post.objects.all()[:3]



class PostDetail(DetailView):
    template_name = "posts/single.html"
    model = Post
    context_object_name = "single"

   # def  get_object(self):
   #     slug = self.kwargs.get("slug")
   #     return Post.objects.get(slug = slug)


@method_decorator(login_required(login_url='/login'),name="dispatch")
class CreatePostView(CreateView):
    template_name = 'posts/create_post.html'
    form_class = CreatePostForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return  super(CreatePostView,self).form_valid(form)


@method_decorator(login_required(login_url='/login'),name="dispatch")
class PostDeleteView(DeleteView):
    model= Post
    success_url = '/'
    template_name = 'posts/delete.html'

    def delete(self,request,*args,**kwargs):
        self.object = self.get_object()
        if self.object.user == request.user:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        else:
            return HttpResponseRedirect('/')

    def get(self,request,*args,**kwargs):
        self.object = self.get_object()
        if self.object.user != request.user:
            return HttpResponseRedirect('/')
        return super(PostDeleteView,self).get(request,*args,*kwargs)




'''
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

'''

# Methodlar


def single(request,slug):
    post = get_object_or_404(Post,slug=slug)
    return render(request,'posts/single.html',{'single' : post })


def index(request):
    allPosts  = Post.objects.all()
    return render(request,'posts/index.html',{'posts': allPosts})


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




















