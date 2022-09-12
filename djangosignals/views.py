from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    a=10/2
    return HttpResponse('helo')