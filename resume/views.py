from django.shortcuts import render
from .models import portfolio

# Create your views here.

def index(request):
    return render(request,"index.html")


def form(request):
    if request.method== 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data = portfolio(name=name,email=email,subject=subject,message=message)
        # if data.is_valid():
        data.save()
        return render(request,'index.html',{'message':"Your message has been sent. Thank you!"})

