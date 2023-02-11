from django.urls import path
from .views import categories, catalog


urlpatterns = [
    path('', categories, name='categories'),
    path('products/<int:category_id>', catalog, name='products'),
    path('page/<int:category_id>/<int:page>/', catalog, name='paginator'),

]



