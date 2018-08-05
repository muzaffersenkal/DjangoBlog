from django import forms
from .models import Post


class CreatePostForm(forms.ModelForm):
    baslik = forms.CharField(label='Başlık',max_length=200)

    class Meta:
        model = Post
        fields = ('title','content','image')