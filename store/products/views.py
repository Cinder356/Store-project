from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
# import requests
# from bs4 import BeautifulSoup
from django.urls import reverse

from products.models import Category, Product, Basket


# from random import choice


def get_curs():
    # link = 'https://webservice.1prime.ru/pttable?host=1prime.ru&encoding=utf-8&template=prime_gold_site3_jsonp&time=14739380'
    # responce = requests.get(link)
    # data = responce.json()
    # return data[0]['value']
    return '70'



def index(request):
    return render(request, 'products/index.html', dict())

# def catalog(request):
#     return render(request, 'products/products.html', dict(curs=get_curs(), range=range(3)))


def categories(request):
    categories_list = Category.objects.all()
    context = dict(categories=categories_list)

    return render(request, 'products/categories.html', context)


def catalog(request, category_id, page=1):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category_id)
    per_page = 1
    paginator = Paginator(products,per_page)
    products_paginator = paginator.page(page)
    return render(request, 'products/catalog.html', dict(products=products_paginator, category=category))


def basket(request, product_id):
    product = Product.objects.get(id=product_id)
    user_baskets = Basket.objects.filter(user=request.user, product=product)

    if not user_baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)

    else:
        basket = user_baskets.last()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_watch(request):
    basket = Basket.objects.filter(user=request.user)
    context = dict(basket=basket)
    return render(request, 'products/basket.html', context)


