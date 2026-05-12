from distutils.command.upload import upload
from enum import unique
from django.db import models
from django.utils import timezone
# Create your models here.
class BlogDb(models.Model):
    blogtitle=models.CharField(max_length=200, unique=True)
    blogcontent=models.TextField()
    blogauthor=models.CharField(max_length=200)
    postdate=models.DateTimeField(auto_now_add=True)
    picture=models.ImageField(default='default.png',upload_to="uploads", null=True, blank=True)
    
    def __str__(self):
        return self.blogtitle
        