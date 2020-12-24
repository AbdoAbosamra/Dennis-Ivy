from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.registerPage , name = 'register'),
    path('login/', views.loginPage , name = 'login'),
    path('logout/', views.logoutUser , name = 'logout'),


    path('', views.home , name = 'home'),
    path('user/' ,views.user ,name = 'user')
    path('products/',views.products , name = 'products'),
    path('customer/<str:pk_test>',views.customer , name = 'customer' ),
    path('createOrder/<str:pk>' , views.createOrder ,name = 'createOrder'),
    path('UpdateOrder/<str:pk>' , views.UpdateOrder ,name = 'UpdateOrder'),
    path('deleteOrder/<str:pk>' , views.deleteOrder ,name = 'deleteOrder'),


]