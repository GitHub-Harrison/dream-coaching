from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import Product, Category, ProductReview
from .forms import ProductForm, ProductBookingForm, ReviewForm


# Create your views here.


def all_products(request):
    """ a view to show all coaching packages, sorting and searching """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    # handle search box, category filter, sort by price/tier/duration
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'search-box' in request.GET:
            query = request.GET['search-box']
            if not query:
                messages.error(request, "The search box was empty")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ a view to show product detail page of product when clicked """

    product = get_object_or_404(Product, pk=product_id)
    product_booking_form = ProductBookingForm()

    # review
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, 'Your review was successfully added!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            print(form.errors)
            messages.error(request, 'Failed to submit your review')
    else:
        form = ReviewForm()

    template = 'products/product_detail.html'
    context = {
        'product': product,
        'product_booking_form': product_booking_form,
        'form': form,
    }

    return render(request, template, context)


@login_required()
def add_product(request):
    """ add product admin form """
    if not request.user.is_superuser:
        messages.error(request, 'Access denied, invalid permissions')
        return redirect(reverse('products'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Product could not be added. Please check the form and try again.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required()
def edit_product(request, product_id):
    """ edit product admin form """
    if not request.user.is_superuser:
        messages.error(request, 'Access denied, invalid permissions')
        return redirect(reverse('products'))
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully')
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(request, 'Product could not be updated. Please check the form and try again.')
    else:
        form = ProductForm(instance=product)

    template = 'products/edit_product.html'
    context = {
        'product': product,
        'form': form,
    }

    return render(request, template, context)


@login_required()
def delete_product(request, product_id):
    """ delete product admin form """
    if not request.user.is_superuser:
        messages.error(request, 'Access denied, invalid permissions')
        return redirect(reverse('products'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted successfully')
    return redirect(reverse('products'))
