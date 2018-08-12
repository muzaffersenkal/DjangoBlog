"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as authViews
from posts.views import register,HomeRedirectView,RegisterView
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('login/', authViews.LoginView.as_view(),name="login"),
    path('password/change/', authViews.PasswordChangeView.as_view(template_name='registration/password-change.html'),name="password_change"),
    path('password/change/done', authViews.PasswordChangeDoneView.as_view(template_name='registration/password-change-done.html'),name="password_change_done"),
    path('register/', RegisterView.as_view() ,name="register"),
    path('go-to-home',HomeRedirectView.as_view(),name="go-home"),


    path('logout/',authViews.logout,name="logout")


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)