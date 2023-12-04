from django.contrib.auth.models import User
from django.db import models
from uuid import uuid4
from django.db import models


class Bloguer(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE,blank=True, null=True)
    Bio = models.TextField(max_length=120)


    def __str__(self):
        return self.user.username


class Blog(models.Model):
    title = models.CharField(max_length=30)
    Description = models.CharField(max_length=200)
    Date_publication = models.DateField()
    id_bloguer = models.ForeignKey(Bloguer, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return f"Blog : {self.title}"



class Comments(models.Model):
    Description = models.CharField(max_length=200)
    Date_publication = models.DateTimeField(auto_now_add=True)
    id_bloguer = models.ForeignKey(Bloguer, on_delete=models.CASCADE, blank=True, null=True )
    id_blog = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True, null=True )

    def __str__(self):
        return f" Comments : {self.Description}"
# Create your models here.
