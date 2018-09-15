from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save

# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="profile")

    avatar = models.ImageField(upload_to="uploads/avatars/",default="uploads/avatars/default.jpg")
    follow = models.ManyToManyField("self",blank=True,related_name="userFollow",symmetrical=False)

    slug = models.SlugField(unique=True,editable=False)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.user.username)
        super(UserProfile,self).save(*args,**kwargs)

    def __str__(self):
        return self.user.username

    #takip ettiği kişi sayısı

    def followedCount(self):
        return self.follow.count()

    #takipçi sayısı

    def followersCount(self):
        return self.userFollow.all().count()

def create_user_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)



post_save.connect(create_user_profile,sender=User)