from django.urls import path
from .views import home, product

urlpatterns = [
    path('', home),
    path('product/<int:code>/', product),
]

#request > url > view > model > request