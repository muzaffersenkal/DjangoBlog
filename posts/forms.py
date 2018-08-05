from django import forms
from .models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CreatePostForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super(CreatePostForm,self).__init__(*args,**kwargs)
        self.helper = FormHelper()


        self.helper.add_input(Submit('submit','Submit'))



    class Meta:
        model = Post
        fields = ('title','content','image')