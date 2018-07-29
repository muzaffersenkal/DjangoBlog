from django.db import models
from django.conf import settings
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='uploads/',blank=True)
    content = models.TextField()
    created = models.DateField('date published')

    def __str__(self):
        return  self.title + " => " + str(self.created)