from django.shortcuts import render
from goods.models import Categories, Products

# Create your views here.


def catalog(request):
    all_categories = Categories.objects.all()
    context = {'title': 'Catalog', 'categories': all_categories}
 
    return render(request, 'goods/catalog.html', context=context)


def product(request):
    all_products = Products.objects.all()

    return render(request,'goods/product.html', {'products': all_products})
