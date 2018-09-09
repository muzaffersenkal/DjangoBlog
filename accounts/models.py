from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify

# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="profile")

    avatar = models.ImageField(upload_to="uploads/avatars/",default="uploads/avatars/default.jpg")


    slug = models.SlugField(unique=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.user.username)
        super(UserProfile,self).save(*args,**kwargs)

    def __str__(self):
        return self.user.username
