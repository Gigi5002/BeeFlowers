from django.shortcuts import HttpResponse

from django.db.models import Q

from .models import Product


def index(request, search_item):

    # Create instance
    # flower = Product(
    #     name='ERLAN',
    #     price=1,
    #     description='BILAL',
    #     quantity=1,
    #     rating=1
    # )
    #
    # flower.save()
    #
    # print(flower.id)

    # SELECT * FROM Product
    # flowers = Product.objects.all()

    # SELECT * FROM Product Where id = 1
    # flower = Product.objects.get(name='ERLAN')
    # print(flower)

    # 1 = Авторские букеты
    # 2 = Любимой
    # 3 = Маме
    # для получение введенных значений
    # flowers = Product.objects.filter(price__gt=5000, price__lt=10_000
    # icontains это для того чтобы при вводе пользователем не объязательно букво в букво было )
    flowers = Product.objects.filter(Q(name__icontains=search_item) | Q(description__icontains=search_item))

    return HttpResponse(flowers)
