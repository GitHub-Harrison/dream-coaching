from django.shortcuts import render
from django.contrib import messages

from .models import Contact


def contact_us(request):
    if request.method == 'POST':
        if form.is_valid():
            contact = Contact()
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')

            contact.name = name
            contact.email = email
            contact.message = message
            contact.save()
            messages.success(request, 'Message sent successfully')
        else:
            messages.error(request, 'Message failed to send')

    return render(request, 'contact/contact.html')
