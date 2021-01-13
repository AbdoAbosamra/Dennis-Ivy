from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login ,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import Product ,Customer , Order #Error from no thing if i make it "*"
from .forms import OrderForm ,CreateUserForm
from .filters import OrderFillter
from .decorators import unauthenicated_user , allowed_users ,admin_only
# Create your views here.
@unauthenicated_user
def registerPage(request): 
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name= 'customer') #This for get customer [user group]
            user.groups.add(group) #Add Automatically  New User to customer Group.
            messages.success(request ,'Account was created ' + username )
            return redirect('login')

    context = {'form' : form}
    return render(request , 'accounts/register.html' , context)
def loginPage(request):
    if request.user.is_authenticated: # ! if you are already do login  You can not go again to loin page .
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request , username=username  , password = password)
            if user is not None:
                login(request , user)
                return redirect('home')
            else:
                messages.info(request , 'Username Or Password is incorrect')
    context = {}
    return render(request , 'accounts/login.html', context)
def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login') # if iam not loin before willnot allow me to accss before login.
#@allowed_users(allowed_roles=['admin']) #For allowed which groups in admin page [Groups Of Users].  
@admin_only
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
@login_required(login_url='login') # if iam not loin before willnot allow me to accss before login.
@allowed_users(allowed_roles=['admin']) #For allowed which groups in admin page [Groups Of Users].  

def userPage(request):
    context = {}
    return render(request , 'accounts/user.html' , context)

def products(request):
	products = Product.objects.all()
	return render(request , 'accounts/products.html' , {'products': products})

@login_required(login_url='login') # if iam not loin before willnot allow me to accss before login.
@allowed_users(allowed_roles=['admin']) #For allowed which groups in admin page [Groups Of Users].  

def customer(request ,pk_test):
    customer = Customer.objects.get(id=pk_test)

    
    orders = customer.order_set.all()

    order_count = orders.count()
    
    My_Filter = OrderFillter(request.GET , queryset = orders )
    orders = My_Filter.qs  

    context = {'orders' : orders , 'customer' : customer  , 'order_count' : order_count , 'My_Filter' : My_Filter}
    return render(request , 'accounts/customer.html' ,context)
@login_required(login_url='login') # if iam not loin before willnot allow me to accss before login.
@allowed_users(allowed_roles=['admin']) #For allowed which groups in admin page [Groups Of Users].  

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

@login_required(login_url='login') # if iam not loin before willnot allow me to accss before login.
@allowed_users(allowed_roles=['admin']) #For allowed which groups in admin page [Groups Of Users].  

def UpdateOrder(request,pk):
    order = Order.objects.get(id = pk)
    form  = OrderForm(instance=order)    
    if request.method == 'POST':    
        form = OrderForm(request.POST ,instance=order)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request , 'accounts/order_form.html' ,context)
@login_required(login_url='login') # if iam not loin before willnot allow me to accss before login.
@allowed_users(allowed_roles=['admin']) #For allowed which groups in admin page [Groups Of Users].  

def deleteOrder(request,pk):
    order = Order.objects.get(id = pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {'item': order}
    return render(request , 'accounts/delete.html' ,context)
