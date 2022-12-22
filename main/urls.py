from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    # path("about/",views.about),
    path('productview/<id>/',views.productview),
    path('cart/',views.cart),
    path('update_cart/<id>/',views.update_cart),
]