from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("you are in home page")

def about(request):
    return HttpResponse("you are in about page")

def contacts(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        return render(request,'submit.html', {'fname':fname, 'lname':lname})
    else:
        return render(request,'contacts.html')


