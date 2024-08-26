from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages




# Create your views here.

#-------------------------------------------------
# Index
#-----------------------------------------------

@login_required
def index(request):
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    customer_count = User.objects.all().count()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.client = request.user
            obj.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        'form': form,
        'orders': order,
        'products': product,
        'product_count': product_count,
        'order_count': order_count,
        'customer_count': customer_count,
    }
    return render(request, 'dashboard/index.html', context)


#---------------------------------------------------------
# 1- Customers
#---------------------------------------------------------

@login_required
def customers(request): 
    customers = User.objects.all() # Using ORM
    customer_count = User.objects.all().count()
    product_count = Product.objects.all().count()
    order_count = Order.objects.all().count()


    context = {
        'customers': customers,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/customer.html', context)

#---------------------------------------------------------------------
# Customer Detail
#---------------------------------------------------------------------
@login_required(login_url='user-login')
def customer_detail(request, pk):
    customer = User.objects.all()
    customer_count = customer.count()
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    customers = User.objects.get(id=pk)
    context = {
        'customers': customers,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,

    }
    return render(request, 'dashboard/customers_detail.html', context)


#=============================================================
# 2- Products
#--------------------------------------------------------------

@login_required
def product(request):
    items = Product.objects.all() # Using ORM
    customer_count = User.objects.all().count()
    order_count = Order.objects.all().count()
    product_count = Product.objects.all().count()



    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm()       
    context = {
        'items':items,
        'form': form,
        'customer_count': customer_count,
        'order_count': order_count,
        'product_count': product_count,

    }
    return render(request, 'dashboard/product.html', context)

#------------------------------------------------------------------------
# Delete Product
#-----------------------------------------------------------------------

@login_required
def product_delete(request, pk):
    item = Product.objects.get(id=pk) # To have it prefilled with the current info
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    context = {
        'item': item
    }
    return render(request, 'dashboard/products_delete.html', context)

#----------------------------------------------------------------------------------
# Update Product
#-------------------------------------------------------------------------------

@login_required
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/products_update.html', context)

#-------------------------------------------------------------------------
# Reservations
#-------------------------------------------------------------------------

@login_required
def reservations(request):
    orders = Order.objects.all()
    order_count = orders.count()
    #customer = User.objects.filter(groups=2)
    #customer_count = customer.count()
    customer_count = User.objects.all().count()

    product = Product.objects.all()
    product_count = product.count()

    context = {
        'orders': orders,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/reservations.html', context)

#--------------------------------------------------------------------------
# SAVE INFO
#---------------------------------------------------------------------------
def save_info(request):
    if request.method == 'POST':
        for order in Order.objects.all():
            # Save the date of return
            date_field_name = f'date_of_return_{order.id}'
            date_value = request.POST.get(date_field_name)
            if date_value:
                order.date_of_return = date_value

            # Save the returned status
            returned_field_name = f'returned_{order.id}'
            order.returned = returned_field_name in request.POST  # Checkbox is checked if its name is in POST data

            # Save the order
            order.save()

        messages.success(request, 'Dates and return statuses saved successfully!')
    return redirect('dashboard-order')  # Adjust the redirect URL to your view