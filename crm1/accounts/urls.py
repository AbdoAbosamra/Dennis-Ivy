from django.urls import path
from . import views


urlpatterns = [
    path('', views.home , name = 'home'),
    path('products/',views.products , name = 'products'),
    path('customer/<int:pk>',views.customer , name = 'customer' ),
    path('createOrder/' , views.createOrder ,name = 'createOrder'),
    path('UpdateOrder/<int:pk>' , views.UpdateOrder ,name = 'UpdateOrder'),
    path('deleteOrder/<int:pk>' , views.deleteOrder ,name = 'deleteOrder'),


]