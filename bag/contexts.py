from django.conf import settings
from products.models import Product
from django.shortcuts import get_object_or_404


def bag_contents(request):

    bag_items = []
    total = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():

        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += product.price
            bag_items.append({
                'item_id': item_id,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            total += product.price
            bag_items.append({
                'item_id': item_id,
                'product': product,
                'date': item_data['date'],
            })

    context = {
        'bag_items': bag_items,
        'total': total,
    }

    return context
