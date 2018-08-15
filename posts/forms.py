from django import forms
from .models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Layout,Field,HTML


class CreatePostForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super(CreatePostForm,self).__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.field_class = "mt-10"
        self.helper.layout = Layout(
            Field("title",css_class="single-input",placeholder="Title"),
            HTML("<hr>"),
            Field("category", css_class="single-input"),
            Field("content",css_class="single-input",placeholder="Birşeyler Yazın"),
            Field("image",css_class="single-input"),
        )


        self.helper.add_input(Submit('submit','Yazı Ekle',css_class="nw-btn primary-btn mt-10"))



    class Meta:
        model = Post
        fields = ('title','content','category','image')

class UpdatePostForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super(UpdatePostForm,self).__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.field_class = "mt-10"
        self.helper.layout = Layout(
            Field("title",css_class="single-input",placeholder="Title"),
            HTML("<hr>"),
            Field("category", css_class="single-input"),
            Field("content",css_class="single-input",placeholder="Birşeyler Yazın"),
            Field("image",css_class="single-input"),
        )


        self.helper.add_input(Submit('submit','Yazı Güncelle',css_class="nw-btn primary-btn mt-10"))



    class Meta:
        model = Post
        fields = ('title','content','category','image')