from django.shortcuts import render
from products.models import Product

# Create your views here.
def do_search(request):
    products = Products.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})