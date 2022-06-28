from django.shortcuts import render
from .models import Contact


def contact_us(request):
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact.name = name
        contact.email = email
        contact.message = message
        contact.save

    return render(request, 'contact/contact.html')
