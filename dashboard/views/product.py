from ast import keyword
from itertools import product
from sys import implementation
from django.shortcuts import render,redirect,get_object_or_404
from nursery_ecommerce_app.models.product import Product,ProductGallery
from nursery_ecommerce_app.models.category import Category
from dashboard.froms.product_from import ProductForm
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime
@login_required(login_url='admin_login')
def admin_add_product(request):
    if request.method=="POST":
        form = ProductForm(request.POST,request.FILES)
        #productgeleryform = ProductGeleryForm(request.POST,request.FILES)
        if form.is_valid():
            
            product_name = form.cleaned_data.get('product_name')
            slug = form.cleaned_data.get('slug')
            stock = form.cleaned_data.get('stock')
            description = form.cleaned_data.get('description')
            images = form.cleaned_data.get('images')
            price = form.cleaned_data.get('price')
            label =form.cleaned_data.get('label')
            category = form.cleaned_data.get('category')
            
            
            data = Product.objects.create(product_name=product_name,slug=slug,stock=stock,description=description,images=images,price=price,label=label,category=category)
            data.save()
            #image = productgeleryform.cleaned_data.get('image')
            #gell_data = ProductGallery.objects.create(image=image)
            #gell_data.save()
            return redirect("admin_product_list")
    else:
            form = ProductForm()
            #productgeleryform = ProductGeleryForm()
    context ={
        'form':form,
        #'productgeleryform':productgeleryform,
    }
            
    return render(request,"admin_dashboard/product_add.html",context)
@login_required(login_url='admin_login')
def admin_products_list(request):
    products = Product.objects.all().filter(is_available=True).order_by('id')
    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    product_count = products.count()
    
    context = {
        'products': paged_products,
        'product_count':product_count,

    }
    return render(request,"admin_dashboard/page-products-list.html",context)
def admin_product_delete(request,product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect("admin_product_list")
@login_required(login_url='admin_login')
def admin_edit_product(request,product_id):
    product = Product.objects.get(id=product_id)
    if request.method =="POST":
        form = ProductForm(request.POST,request.FILES,instance=product)
        
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            
            return redirect(reverse('admin_product_list'))
    else:
        form = ProductForm(instance=product)
    context = {
        'form':form,
    }
    return render(request,"admin_dashboard/product_edit.html",context)


