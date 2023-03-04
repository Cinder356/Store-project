from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, ListView

from products.models import Category, Product, Basket


class MainView(TemplateView):
    template_name = 'products/index.html'


class CategoriesListView(ListView):
    model = Category
    template_name = 'products/categories.html'
    context_object_name = 'categories'
    paginate_by = 3


# def categories(request):
#     categories_list = Category.objects.all()
#     context = dict(categories=categories_list)
#
#     return render(request, 'products/categories.html', context)

class ProductsListView(ListView):
    model = Product
    template_name = 'products/catalog.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        category = Category.objects.get(id=category_id)
        return queryset.filter(category=category)

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(self).get_context_data()
    #     context['category'] = Category.objects.get(id=)


def catalog(request, category_id, page=1):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category_id)
    per_page = 1
    paginator = Paginator(products, per_page)
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



def remove_product(request, product_id):
    product = Product.objects.get(id=product_id)
    user_baskets = Basket.objects.filter(user=request.user, product=product)
    basket = user_baskets.last()
    if basket.quantity > 1:
        basket.quantity -= 1
        basket.save()
    else:
        basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def delete_basket(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
