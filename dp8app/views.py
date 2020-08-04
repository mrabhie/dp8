from django.shortcuts import render
from django.http import HttpResponse

def trial(request):
    return HttpResponse('<h1>Project is on air</h1>')

def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,"dp8app/home.html")

def profile(request):
    name="pavan abhilash"
    return render(request,"dp8app/profile.html",{'name':name})
# Create your views here.
