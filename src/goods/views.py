from django.shortcuts import get_list_or_404, render
from django.core.paginator import Paginator

from goods.models import Products

# Create your views here.


def catalog(request, category_slug, page=1):

    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        # Через filter() мы филтруем по категории, обращаясь к полю category
        # ЧЕРЕЗ САМ ТОВАР с помощю ForeignKey()
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    paginator = Paginator(goods, 3)
    current_page = paginator.page(page) # отабражает нужную нам страницу

    
    context = {
        'title': 'Catalog',
        'goods': current_page,
        'slug_url': category_slug
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
