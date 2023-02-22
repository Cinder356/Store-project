from django.urls import path
from .views import categories, catalog, basket, basket_watch

urlpatterns = [
    path('', categories, name='categories'),
    path('products/<int:category_id>', catalog, name='products'),
    path('page/<int:category_id>/<int:page>/', catalog, name='paginator'),
    path('basket/<int:product_id>/',basket, name='basket'),
    path('basket/',basket_watch, name='basket_watch'),

]



