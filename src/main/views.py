from django.shortcuts import render



def index(request):

    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
 
        }

    return render(request, 'main/index.html', context=context)


def about(request):
    return render(request, 'main/about.html', {
        'title': 'About',
        'content': 'About Us',
        'text_on_page': 'Some text about this another ecomerse project lol ;)'
    })