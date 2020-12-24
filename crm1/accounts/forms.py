from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Order

class OrderForm(ModelForm):
    class Meta: #This is Two Main Attributes in the Meta class 
        model = Order # Model = ModelName We will Make from from This stracture.
        fields = '__all__' #Fields we will work with.

class CreateUserForm(UserCreationForm):
    class Meta:
        model= User
        fields = ['username' , 'email'  , 'password1' , 'password2']
