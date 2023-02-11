from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
# import requests
# from bs4 import BeautifulSoup
from products.models import Category, Product
from random import choice


def get_curs():
    # link = 'https://webservice.1prime.ru/pttable?host=1prime.ru&encoding=utf-8&template=prime_gold_site3_jsonp&time=14739380'
    # responce = requests.get(link)
    # data = responce.json()
    # return data[0]['value']
    return '70'



def index(request):
    return render(request, 'products/index.html', dict(curs=get_curs()))

# def catalog(request):
#     return render(request, 'products/products.html', dict(curs=get_curs(), range=range(3)))


def categories(request):
    categories_list = Category.objects.all()
    context = dict(curs=get_curs(),categories=categories_list)

    return render(request, 'products/categories.html', context)

def catalog(request, category_id, page=1):

    products = Product.objects.filter(category=category_id)
    per_page = 1
    paginator = Paginator(products,per_page)
    products_paginator = paginator.page(page)
    return render(request, 'products/catalog.html', dict(curs=get_curs(), products=products_paginator))