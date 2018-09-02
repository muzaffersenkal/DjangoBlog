from django.db import models
from django.conf import settings
# Create your models here.
from django.template.defaultfilters import slugify


class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True,editable=False)


    def __str__(self):
        return self.title

    def postCount(self):
        return self.posts.all().count()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tag, self).save(*args, **kwargs)


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='uploads/',blank=True)
    content = models.TextField()
    slug = models.SlugField(unique=True,editable=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)



    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="posts")
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return  self.title + " => " + str(self.created)

    def commentCount(self):
        return self.comments.all().count()

    def save(self, *args,**kwargs):
        self.slug =  slugify(self.title)
        super(Post,self).save(*args,**kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,default=1,related_name="comments")
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)

    content = models.TextField()

    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username + " => " + self.post.title











