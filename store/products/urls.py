from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *
#cache_page(10)()
urlpatterns = [
    path('', CategoriesListView.as_view(), name='categories'),
    path('products/<int:category_id>', ProductsListView.as_view(), name='products'),
    path('page/<int:category_id>/<int:page>/', ProductsListView.as_view(), name='paginator'),
    path('basket/<int:product_id>/', basket, name='basket'),
    path('basket/', basket_watch, name='basket_watch'),
    path('basket/remove/<int:product_id>/', remove_product, name='remove_product'),
    path('basket/delete/<int:basket_id>/', delete_basket, name='delete_basket'),

]

