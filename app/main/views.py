from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories


def index(request):



    context: dict[str,str] = {
        'title': 'Домошняя - Главная',
        'content': 'Интернет-магазин Вязаных Изделий for PolLis',


    }

    return render(request, 'main/index.html', context)

def about(request):
    context: dict[str, str] = {
        'title': 'Информация о Магазине',
        'content': 'О НАС',
        'text_on_page': "Добро пожаловать в интнрнет-магазин стильных вещей ручной работы for PolLis. "
                        "Качество изделий-это главный приоритет нашего магазина."
                        "Все вещи создаются из высококачественных материалов. "
                        "Каждое изделие тщательно прорабатывается, что гарантирует его долговечность. "
                        "Весь товар магазина - это только ручная вязка, а значит уникальность каждого изделия. "
                        "Кроме того мы предлагаем возможность заказать вещи по индивидуальным меркам"
                        "Интернет-магазин for PolLis предоставляет возможность сделать покупку быстро и легко, "
                        "не выходи из дома. Доставка осуществляется в любую точку РФ. "
                        "Видео с моими работами вы можете посмотреть на моём YouTube-канале."
    }

    return render(request, 'main/about.html', context)

def contact(request):
    context = {
        'title': "Контактная информация",
        'content': "Контакты",
        'text_on_page': 'erkgtjnergeogherle',
    }

    return render(request, 'main/contact.html', context)
# Create your views here.
