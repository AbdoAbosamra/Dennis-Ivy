from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta: #This is Two Main Attributes in the Meta class 
        model = Order # Model = ModelName We will Make from from This stracture.
        fields = '__all__' #Fields we will work with.