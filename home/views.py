from django.shortcuts import render
from django.contrib import messages

from .models import NewsletterUser
from .forms import NewsletterSignUpForm


def index(request):
    """ a view to return the index page """

    return render(request, 'home/index.html')


def newsletter_signup(request):
    form = NewsletterSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.info(request, 'It appears this email is already subscribed to our newsletter!')
        else:
            messages.success(request, 'Your email has been successfully added to our newsletter list!')
            instance.save()

    template = 'home/index.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
