from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    created = models.DateField('date published')

    def __str__(self):
        return  self.title + " => " + str(self.created)