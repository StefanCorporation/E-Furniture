from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html', {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME'
        })


def about(request):
    return render(request, 'main/about.html', {
        'title': 'About',
        'content': 'About Us',
        'text_on_page': 'Some text about this another ecomerse project lol ;)'
    })