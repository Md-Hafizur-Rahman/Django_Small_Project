import email
from django.shortcuts import render,HttpResponse
from .models import User,Page,Like,Post,Nasheed

# Create your views here.
def home(request):
    return render (request,"relationPaPP/home.html")
def show_user_data(request):
    data1=User.objects.all()
    data2=User.objects.filter(user_name='hafizur')
    data3=User.objects.filter(page__page_cat="video")
    data4=User.objects.filter(post__post_publish_date="2022-09-11")
    data5=User.objects.filter(post__post_cat='book')
    # data5=User.objects.get(nasheed__nasheed_duration=5)
    return render(request,"relationPaPP/user.html",{'data1':data1,'data2':data2,'data3':data3,'data4':data4,'data5':data5})

def show_page_data(request):
    data1=Page.objects.all()
    data2=Page.objects.filter(page_cat="video")
    data3=Page.objects.filter(user__user_name='hafizur')
    return render(request,"relationPaPP/page.html",{'data1':data1,'data2':data2,'data3':data3})
def show_post_data(request):
    data1=Post.objects.all()
    data2=Post.objects.filter(user__user_name='hafizur')
    data3=Post.objects.filter(post_cat='book')
    # data4=Post.objects.filter(nasheed__nasheed_duration=4.17)
    return render(request,"relationPaPP/post.html",{'data1':data1,'data2':data2,'data3':data3})
def show_nasheed_data(request):
    data1=Nasheed.objects.all()
    data2=Nasheed.objects.filter(user__user_name='hafizur')
    data3=Nasheed.objects.filter(nasheed_duration=5)
    return render(request,"relationPaPP/nasheed.html",{'data1':data1,'data2':data2,'data3':data3})