from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ a view to return the bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add an item to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})
    if 'date' in request.POST:
        date = request.POST.get('date')

    if date:
        bag[item_id] = {'date': date}
    else:
        bag[item_id] = item_id

    messages.success(request, 'added to bag')
    redirect_url = request.POST.get('redirect_url')
    request.session['bag'] = bag

    return redirect(redirect_url)
