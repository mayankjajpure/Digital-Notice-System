from cmath import log
from multiprocessing import context
from telnetlib import LOGOUT
from turtle import pos
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import Feedback, Posts,Category,notice
# Create your views here admin is derik.    
# user jmayank o.
from django.contrib.auth.models import User

def registor(request):
    if request.method=="POST":
      
        name=request.POST.get('name')
        passw=request.POST.get('pass')
      
        user = User.objects.create_user(name,'lennon@thebeatles.com',passw)
        # print(user)
        user.save()
        return render(request,'landing.html')
        
    else:
      
        return render(request,'login')

    
    

def category(request,url):
    cat=Category.objects.get(url=url)
    
    posts=Posts.objects.filter(cat=cat)
    

    data={'post':posts,'cat':cat,}

    return render(request,'category.html',data)
def contact(request):
    var=Category.objects.all()
    data={'var':var,}
    return render(request,'contact.html',data)
def about(request):
    var=Category.objects.all()
    data={'var':var,}
    return render(request,'about.html',data)

def base(request):
    var=Category.objects.all()
    data={'var':var,}
    return render(request,'home.html',data)

def landing(request):
    return render(request,'landing.html')

def home(request):
    return render(request,'login.html')
    
def register(request):
    return render(request,'registration.html')

def send(request):return render(request,'send notice.html')

def loginuser(request):
    var=Category.objects.all()
    
    if request.method=="POST":
        
    
        name=request.POST.get('name')
        passw=request.POST.get('password')
        user = authenticate(request, username=name, password=passw)
        if user is not None:
            var=Category.objects.all()
            data={'var':var,}
            login(request, user)
            return render(request,'home.html',data)

        else:
            print(name,passw)
            return render(request,'login.html')
    else:
    
        return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return render(request,'landing.html')



def feeds(request):
    
    var=Posts.objects.all()
    context={'post':var}
    return render(request,'feeds.html',context)

def showpost(request,url):
    pst=Posts.objects.get(url=url)
    data={'post':pst}
    
    return render(request,'post.html',data)


def sendnotice(request):
    if request.method=='POST':
        head=request.POST['heading']
        cont=request.POST['content']
        nobj=notice(head=head,content=cont)
        nobj.save()    
    return render(request,'send notice.html')



def feedbck(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        cont=request.POST['content']
        fb=Feedback(name=name,mail=email,feed=cont)
        fb.save()
    return render(request,'contact.html')