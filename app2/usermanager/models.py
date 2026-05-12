from django.db import models
from django.contrib.auth.models import User

from blogs.models import BlogDb

# Create your models here.
class ProfileModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,)
    profile_pic=models.ImageField(default="default.jpg", upload_to="uploads",blank=True,null=True)
    bio=models.TextField(blank=True, null=True, max_length=200)
    facebook=models.CharField(max_length=200, blank=True,null=True)
    instagram=models.CharField(max_length=200, blank=True,null=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"

class Comment(models.Model):
    blog=models.ForeignKey(BlogDb,related_name="comments",on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    comment_time=models.DateTimeField(auto_now=True)        

    def save(self,*args,**kwargs):
        return super(Comment,self).save(*args,**kwargs )

    def __str__(self) -> str:
        return self.blog.blogtitle

class Like(models.Model):
    blog=models.ForeignKey(BlogDb,related_name="reactions",on_delete=models.CASCADE)
    author=models.TextField()
    react=models.ManyToManyField(User)   

    def save(self,*args,**kwargs):
        return super(Like,self).save(*args,**kwargs)

    def __str__(self) -> str:
        return self.blog.blogtitle