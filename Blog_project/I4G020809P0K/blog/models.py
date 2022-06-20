

# Create your models here.
from django.conf import Settings
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    Text = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    Created_date = models.DateTimeField(auto_now= True)
    Published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
