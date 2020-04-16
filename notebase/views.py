from django.shortcuts import render
from django.http import HttpResponse
from .models import data
# Create your views here.
def index(request):
    return(render(request,'notesbase.html'))

def add(request):
    d=data()
    d.date=request.GET['date']
    d.title=request.GET['title']
    d.story=request.GET['story']
    d.save()
    dis = data.objects.all()
    return(render(request,'display.html',{'dis':dis}))

