from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm
from django.contrib.auth.models import User



# Create your views here.

#-------------------------------------------------
# Index
#-----------------------------------------------

@login_required
def index(request):
    return render(request, 'dashboard/index.html',context)


#---------------------------------------------------------
# Customers
#---------------------------------------------------------

@login_required
def staff(request): 
    
    
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    context = {
        'customer': customer,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/staff.html')


#=============================================================
# Products
#--------------------------------------------------------------

@login_required
def product(request):
    items = Product.objects.all() # Using ORM

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
# Order
#-------------------------------------------------------------------------

@login_required
def order(request):
    return render(request, 'dashboard/order.html')

