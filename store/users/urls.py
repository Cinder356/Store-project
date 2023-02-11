

from django.urls import path
from .views import auth_user, register


urlpatterns = [
    path('authorization', auth_user, name='auth'),
    path('regostration', register, name='register'),
]
