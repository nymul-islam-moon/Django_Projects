from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from first_app.models import Contact

# Create your views here.

def home(request):
    #return HttpResponse("<h1>This is home page</h1> <a href='contact/'>Contact</a> <a href='about/'>About</a> ")
    return render(request, 'home.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
    #return HttpResponse("<h1>This is contact page</h1> <a href='/'>Home</a> <a href='/about/'>About</a> <a href='/services/'>Services</a>")
    return render(request, 'contact.html')


def about(request):
    #return HttpResponse("<h1>This is About us</h1> <a href='/'>Home</a> <a href='/contact/'>Contact</a> <a href='/services/'>Services</a>")
    return render(request, 'about.html')

def services(request):
    #return HttpResponse("<h1>This is Services</h1> <a href='/'>Home</a> <a href='/contact/'>Contact</a> <a href='/about/'>About</a>")
    return render(request, 'services.html')

def beach(request):
    #return HttpResponse("<h1>This is Services</h1> <a href='/'>Home</a> <a href='/contact/'>Contact</a> <a href='/about/'>About</a>")
    return render(request, 'beach.html')

def blue(request):
    #return HttpResponse("<h1>This is Services</h1> <a href='/'>Home</a> <a href='/contact/'>Contact</a> <a href='/about/'>About</a>")
    return render(request, 'blue-sky.html')

def other(request):
    #return HttpResponse("<h1>This is Services</h1> <a href='/'>Home</a> <a href='/contact/'>Contact</a> <a href='/about/'>About</a>")
    return render(request, 'other.html')