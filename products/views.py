from django.shortcuts import render

# Create your views here.

def all_packages(request):
    """ a view to show all coaching packages, sorting and searching """

    return render(request, 'products/products.html', context)
