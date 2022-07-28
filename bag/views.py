from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
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


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
