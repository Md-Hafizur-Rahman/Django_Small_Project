from django.urls import path ,include 
from djangosignals import views
urlpatterns = [
    path('index/',views.index),
    
]