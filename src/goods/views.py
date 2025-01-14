from django.shortcuts import get_list_or_404, render
from django.core.paginator import Paginator

from goods.models import Products

# Create your views here.


def catalog(request, category_slug):

    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)



    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        # Через filter() мы филтруем по категории, обращаясь к полю category
        # ЧЕРЕЗ САМ ТОВАР с помощю ForeignKey()
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    if on_sale:
        goods = Products.objects.filter(discount__gt=0) # если скидка выше 0

    if order_by and order_by != 'default':
        goods = goods.order_by(order_by) # через метод order_by возвращаем сортировку либо от 
                                                    # меньшего к большому либо наоборот


    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page)) # отабражает нужную нам страницу

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
