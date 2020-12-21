from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import Product ,Customer , Order #Error from no thing if i make it "*"
from .forms import OrderForm
# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()

    deliverd = orders.filter(status ='Delivered').count()
    pending = orders.filter(status = 'Pending').count()

    context = {'orders' : orders , 'customers' : customers  , 
    'total_orders': total_orders , 'deliverd' : deliverd , 'pending' : pending}
    return render(request , 'accounts/dashboards.html' , context)

def products(request):
	products = Product.objects.all()
	return render(request , 'accounts/products.html' , {'products': products})
def customer(request ,pk_test):
    customer = Customer.objects.get(id=pk_test)

    
    orders = customer.order_set.all()

    order_count = orders.count()

    context = {'orders' : orders , 'customer' : customer  , 'order_count' : order_count}
    return render(request , 'accounts/customer.html' ,context)

def createOrder(request ,pk):
    OrderFormSet = inlineformset_factory(Customer , Order ,fields=('product','status') , extra=10)
    customer = Customer.objects.get(id=pk)
    #form = OrderForm(initial={'customer' : customer})   #for inatial value of the customer when reload the page.
    formset = OrderFormSet(queryset=Order.objects.none(),instance= customer) # To remove inatial in the form and start with none
    if request.method == 'POST':
        formset = OrderFormSet(request.POST , instance= customer )
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset': formset}
    return render(request , 'accounts/order_form.html' ,context)


def UpdateOrder(request,pk):
    order = Order.objects.get(id = pk)
    form  = OrderForm(instance=order)    
    if request.method == 'POST':    
        form = OrderForm(request.POST ,instance=order)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request , 'accounts/order_form.html' ,context)

def deleteOrder(request,pk):
    order = Order.objects.get(id = pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {'item': order}
    return render(request , 'accounts/delete.html' ,context)
