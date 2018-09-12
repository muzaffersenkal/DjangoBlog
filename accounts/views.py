from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView,DetailView
from .models import UserProfile
# Create your views here.


@method_decorator(login_required(login_url="/login"),name="dispatch")
class MyProfileView(TemplateView):
    template_name = "profile/index.html"


    def get_context_data(self, **kwargs):
        context = super(MyProfileView,self).get_context_data(**kwargs)
        context["profile"] = UserProfile.objects.get(user=self.request.user)
        return context


@method_decorator(login_required(login_url="/login"), name="dispatch")
class ProfileView(DetailView):
    model = UserProfile
    template_name = "profile/view.html"
    context_object_name = "profile"