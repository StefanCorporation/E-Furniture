from django.shortcuts import render
from goods.models import Products

# Create your views here.


def catalog(request, category_slug):

    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        # Через filter() мы филтруем по категории, обращаясь к полю category
        # ЧЕРЕЗ САМ ТОВАР с помощю ForeignKey()
        goods = Products.objects.filter(category__slug=category_slug) 

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
