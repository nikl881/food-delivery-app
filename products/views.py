from django.shortcuts import render
from .models import Product

# Views for products.

def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})