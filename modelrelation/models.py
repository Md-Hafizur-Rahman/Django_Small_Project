from re import T
from django.db import models

# Create your models here.
class User(models.Model):
    user_name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.user_name)
    
class Page(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    page_name=models.CharField(max_length=70)
    page_cat=models.CharField(max_length=70)
    favourite=models.BooleanField(default=False)
    page_publish_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
class Like(Page):
    connect=models.OneToOneField(Page, on_delete=models.CASCADE,primary_key=True,parent_link=True)
    count=models.IntegerField()