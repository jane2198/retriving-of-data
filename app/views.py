from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
# Create your views here.
def display_topic(request):
    topics=topic.objects.all()
    d={'topics': topics}
    return render(request,'display_topic.html',d)
def display_web(request):
    T=webpage.objects.all()
    T=webpage.objects.filter(topic_name='cricket')
    T=webpage.objects.exclude(topic_name='football')
    T=webpage.objects.all().order_by('name')
    T=webpage.objects.all().order_by('-name')
    T=webpage.objects.all().order_by(Length('name'))
    T=webpage.objects.all().order_by(Length('name').desc())
    T=webpage.objects.all()[0:2:1]
    T=webpage.objects.all()[:4]
    #T=webpage.objects.all()[-3]

    d={'webpages':T}
    return render(request,'display_web.html',d)
def display_access(request):
    A=AccessRecords.objects.all()
    d={'access':A}
    return render(request,'display_access.html',d)
