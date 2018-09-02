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
from . import views
from django.urls import path
from .views import CreatePostView,IndexView,BlogView,PostDetail,PostDeleteView,UpdatePostView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('detail/<slug:slug>', views.PostDetail.as_view(),name='single'),
    path('detail/<slug:slug>/delete', views.PostDeleteView.as_view(),name='delete'),
    path('detail/<slug:slug>/update', views.UpdatePostView.as_view(),name='update'),
    path('create/', CreatePostView.as_view(), name="createPost"),
    path('blog/', BlogView.as_view(), name="blog"),

    #category
    path('category/<slug:slug>', views.CategoryDetail.as_view(),name='category-detail'),

    path('comment/<int:pk>/delete',views.CommentDeleteView.as_view(),name="comment-delete")

]
