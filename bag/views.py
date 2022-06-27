from django.shortcuts import render

# Create your views here.

def bag(request):
    """ a view to return the bag page """

    return render(request, 'bag/bag.html')
