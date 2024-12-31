from django.shortcuts import render

from goods.models import Categories


def index(request, category_slug):

    if category_slug == 'all':
        category_slug = Categories.objects.all()
    else:
        category_slug = Categories.objects.get(slug=category_slug)

    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
        'category': category_slug
 
        }

    return render(request, 'main/index.html', context=context)


def about(request):
    return render(request, 'main/about.html', {
        'title': 'About',
        'content': 'About Us',
        'text_on_page': 'Some text about this another ecomerse project lol ;)'
    })