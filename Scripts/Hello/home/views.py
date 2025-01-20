from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Contact
from django.contrib import messages

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("this is services page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        contact_info = request.POST.get('Contact')
        desc = request.POST.get('Desc')

        # Validation to ensure 'name' is not empty
        if not name:
            return render(request, 'contact.html', {'error': 'Name cannot be empty'})

        # Save the form data to the database
        contact = Contact(name=name, email=email, contact=contact_info, desc=desc, date=datetime.today())
        contact.save()

        # Redirect or show a success message
        messages.success(request, "Your message has been send!" )

    # If GET request, render the contact form
    return render(request, 'contact.html')
