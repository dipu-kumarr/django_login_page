from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product,Customer,Collection, Order

def say_hello(request):
    queryset = Order.objects.filter(customer_id__in=[75]).filter(id__in=[1,2,10])  # Get all products with unit_price between 1 and 10
    product_count = Product.objects.count()  # Get the total count of products
    return render(request, 'hello.html', {'name': 'dipu', 'products': list(queryset), 'product_count': product_count})
