import site
from django.contrib import admin
from django.urls import path ,include 
from relationproject import views

urlpatterns= [
    
    path("admin/",admin.site.urls),
    path("home/",views.home,name='home'),
    path("user/",views.show_user_data,name='user'),
    path("page/",views.show_page_data,name='page'),
    path("post/",views.show_post_data,name='post'),
    path("nasheed/",views.show_nasheed_data,name='nasheed'),
    

]