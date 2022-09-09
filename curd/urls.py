from django.contrib import admin
from django.urls import path 
from .views import GeeksCreate,GeeksList,GeeksDetailView,GeeksUpdateView,GeeksDeleteView

urlpatterns = [
    path('create/',GeeksCreate.as_view()),
    path('getRe/',GeeksList.as_view(),name="geeksmodel_list"),
    path('<pk>/', GeeksDetailView.as_view()),
    path('<pk>/update', GeeksUpdateView.as_view()),
    path('<pk>/delete/', GeeksDeleteView.as_view()),
     
    ]