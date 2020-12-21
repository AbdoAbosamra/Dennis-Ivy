from django.urls import path
from . import views


urlpatterns = [
    path('', views.home , name = 'home'),
    path('products/',views.products , name = 'products'),
    path('customer/<str:pk_test>',views.customer , name = 'customer' ),
    path('createOrder/<str:pk>' , views.createOrder ,name = 'createOrder'),
    path('UpdateOrder/<str:pk>' , views.UpdateOrder ,name = 'UpdateOrder'),
    path('deleteOrder/<str:pk>' , views.deleteOrder ,name = 'deleteOrder'),


]