from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    reviews = Review.objects.filter(product=product)

    if pk in request.session['reviewed_products']:
        form = ReviewForm()
    else:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                clean_review = form.cleaned_data
                Review.objects.create(text=clean_review['text'], product=product)
                request.session['reviewed_products'].append(pk)
        else:
            form = ReviewForm()

    context = {
        'form': form,
        'product': product,
        'reviews': reviews
    }

    return render(request, template, context)
