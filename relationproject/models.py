from re import T
from django.db import models

# Create your models here.
class User(models.Model):
    user_name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.user_name)
    
class Page(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE) # OneToOne Relationship
    page_name=models.CharField(max_length=70)
    page_cat=models.CharField(max_length=70)
    favourite=models.BooleanField(default=False)
    page_publish_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
class Like(Page):
    connect=models.OneToOneField(Page, on_delete=models.CASCADE,primary_key=True,parent_link=True) # used parent_link for inheritance
    count=models.IntegerField()
class Post(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    post_title=models.CharField(max_length=70)
    post_cat=models.CharField(max_length=70)
    post_publish_date=models.DateField(auto_now_add=True)
    
class Nasheed(models.Model):
    user=models.ManyToManyField(User)
    nasheed_name=models.CharField(max_length=70)
    nasheed_duration=models.IntegerField(null=True)
    
    def writen_by(self):
        p= ",".join(str(p) for p in self.user.all()) # to showing this user value in the admin.py file and showing in the tabale
        # print(p)
        return p
        