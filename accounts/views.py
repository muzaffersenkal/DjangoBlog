from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
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


    def get_context_data(self, **kwargs):
        context = super(ProfileView,self).get_context_data(**kwargs)

        myprofile = self.request.user.profile.get()

        if myprofile.follow.filter(slug=self.get_object().slug):
            context["followStatus"] = "unfollow"

        else:
            context["followStatus"] = "follow"


        return context



def FollowProfile(request,slug):


        if request.method == 'POST':

                status = request.POST.get("status")
                userSlug = request.POST.get("user")
                user = get_object_or_404(UserProfile,slug=userSlug)
                myprofile = request.user.profile.get()
                if status == 'follow':

                    myprofile.follow.add(user)
                    lastStatus = "Takip Edildi"


                else:
                    myprofile.follow.remove(user)
                    lastStatus = "Takip Bırakıldı"

                data = {
                    "status": lastStatus
                }

                return JsonResponse(data)















