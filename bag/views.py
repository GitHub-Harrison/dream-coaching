from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ a view to return the bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add an item to the shopping bag """

    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    request.session['bag'] = bag

    return redirect(redirect_url)
