from django.shortcuts import render
from goods.models import Categories, Products

# Create your views here.


def catalog(request):
    goods = Products.objects.all()

    context = {
        'title': 'Catalog',
        'goods': goods,
        }
 
    return render(request, 'goods/catalog.html', context=context)



def product(request, product_slug=None, product_id=None):
    
    if product_slug:
        product = Products.objects.get(slug=product_slug)
    else:
        product = Products.objects.get(id=product_id)


    context = {
        'product': product
    }

    return render(request,'goods/product.html', context=context)
