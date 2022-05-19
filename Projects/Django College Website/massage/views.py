from django.shortcuts import render,HttpResponse
from datetime import datetime
from massage.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("this is index page")

def service(request):
    return render(request,'service.html')
    #return HttpResponse("this is service page")
    
def civil(request):
    return render(request,'civil.html')  

def electrical(request):
    return render(request,'electrical.html')  

def mechanical(request):
    return render(request,'mechanical.html')

def electronics(request):
    return render(request,'electronics.html')

def first_year(request):
    return render(request,'first_year.html')

def second_year(request):
    return render(request,'second_year.html')

def contact(request):
    if request.method=="POST":
       name=request.POST.get('name')
       email=request.POST.get('email')
       phone=request.POST.get('phone')
       desc=request.POST.get('desc') 
       contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
       contact.save()
       messages.success(request, 'Your Massage Has been sent!.')
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')
