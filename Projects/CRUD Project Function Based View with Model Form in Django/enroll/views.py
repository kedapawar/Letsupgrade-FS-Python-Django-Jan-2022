from django.http.response import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from .forms import StudentRegistration
from .models import User
# Create your views here.
#This Function Of Add & Show all Data
def addshow(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            fm.save()
            fm=StudentRegistration()
    else:
        fm=StudentRegistration()  
    stud=User.objects.all()  
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})

# This Is The Function Of Update Data    

def update_data(request,id):
    if request.method=='POST':
     pi=User.objects.get(pk=id)
     fm=StudentRegistration(request.POST,instance=pi)
     if fm.is_valid():
         fm.save()  
    else:
      pi=User.objects.get(pk=id)
      fm=StudentRegistration(instance=pi)        
    return render(request,'enroll/updates.html', {'form':fm})


# This Is The Function Of Delete Data

def delete_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')
