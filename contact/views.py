from django.shortcuts import render
from django.contrib import messages

from .models import Contact
from .forms import ContactForm


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            messages.success(request, 'Message sent successfully')
        else:
            messages.error(request, 'Message failed to send')

    return render(request, 'contact/contact.html')
