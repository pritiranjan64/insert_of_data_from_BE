from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *

def insert_topic(request):
    tn=input('enter tn')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('topic is created successfully')  


def insert_webpage(request):
    tn=input('enter tn')
    TO1=Topic.objects.get_or_create(topic_name=tn)[0]
    TO1.save()

    n=input('enter name')
    u=input('enter url')
    e=input('enter email')
    WO=Webpage.objects.get_or_create(topic_name=TO1,name=n,url=u,email=e)[0]
    WO.save()
    return HttpResponse('webpage is created successfully') 


def insert_access(request):
    tn=input('enter tn')
    TO2=Topic.objects.get_or_create(topic_name=tn)[0]
    TO2.save()

    n=input('enter name')
    u=input('enter url')
    e=input('enter email')
    WO1=Webpage.objects.get_or_create(topic_name=TO2,name=n,url=u,email=e)[0]
    WO1.save()

    d=input('enter date')
    a=input('enter author')
    AO=AccessRecord.objects.get_or_create(name=WO1,date=d,author=a)[0]
    AO.save()

    return HttpResponse('access is created successfully') 

    
