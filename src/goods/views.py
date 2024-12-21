from django.shortcuts import render
from goods.models import Categories, Products

# Create your views here.


def catalog(request):
    goods = Products.objects.all()

    context = {
        'title': 'Catalog',
        'goods': goods
        }
 
    return render(request, 'goods/catalog.html', context=context)



def product(request):
    all_products = Products.objects.all()

    context = {
        'products': all_products
    }

    return render(request,'goods/product.html', context=context)
