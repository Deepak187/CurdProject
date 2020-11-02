from django.shortcuts import render,redirect
from .models import User
from .forms import StudentRegistration

# Create your views here.
def add_show(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            nm=form.cleaned_data['name']
            em=form.cleaned_data['email']
            pw=form.cleaned_data['password']
            data=User(name=nm,email=em,password=pw)
            data.save()
            form = StudentRegistration()
    else:
        form = StudentRegistration()
    stu= User.objects.all()
    return render(request, 'enroll/addandshow.html',{'form':form, 'stu':stu}) 


def delete_data(request,id):
    if request.method == 'POST':
        pi= User.objects.get(pk=id)
        pi.delete()
    return redirect('/')

def update_data(request,id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=pi)
        if form.is_valid(): 
            form.save()
    else:
        pi=User.objects.get(pk=id)
        form =StudentRegistration(instance=pi)
    return render(request, 'enroll/updatestudent.html',{'form':form})


        