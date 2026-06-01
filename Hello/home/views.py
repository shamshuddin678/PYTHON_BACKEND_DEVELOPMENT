from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    # here this is a dictionary stored
    content = {  
        "variable1" : "ALL Set perfectly",
        "variable2" : "Setter be programmically"
    }
    # messages.success(request,"this is a text message")
    return render(request,"index.html",content)
    # return render(request,"index.html",{'name' : "shamshuddin"})
    # return HttpResponse('this is a home page')

def about(request):
    # return HttpResponse('this is about page')
    return render(request,"about.html")

def services(request):
    # return HttpResponse('this is services page')
    return render(request,"services.html")

def contact(request):
    if(request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        Phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name,email = email,Phone = Phone,desc=desc,date = datetime.today())
        contact.save()
        messages.success(request,"your message has been sent!")
    return render(request,"contact.html")
    # return HttpResponse('this is contact page')