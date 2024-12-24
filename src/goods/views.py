from django.shortcuts import render
from goods.models import Categories, Products

# Create your views here.


def catalog(request):
    goods = Products.objects.all()
    categories = Categories.objects.all() 

    context = {
        'title': 'Catalog',
        'goods': goods,
        'categories': categories
        }
 
    return render(request, 'goods/catalog.html', context=context)



def product(request):
    goods = Products.objects.all()

    context = {
        'products': goods
    }

    return render(request,'goods/product.html', context=context)
