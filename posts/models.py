from django.db import models
from django.conf import settings
# Create your models here.
from django.template.defaultfilters import slugify

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='uploads/',blank=True)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return  self.title + " => " + str(self.created)

    def save(self, *args,**kwargs):
        self.slug =  slugify(self.title)
        super(Post,self).save(*args,**kwargs)