from ast import keyword
from calendar import c
from django.shortcuts import render
from nursery_ecommerce_app.models.product import Product
from nursery_ecommerce_app.models.category import Category
from nursery_ecommerce_app.models.customer import Contact
from nursery_ecommerce_app.models.order import Order,OrderProduct
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
def admin_dashboard(request):
    products = Product.objects.all().filter(is_available=True).order_by('id')
    product = Product.objects.all()
    categories = Category.objects.all()
    context ={
        'products':products,
        'categories':categories,
        'product':product,

    }
    return render(request,"admin_dashboard/index.html",context)
def admin_product_order(request):
    return render(request,"admin_dashboard/page-orders-1.html")
def admin_serach(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            

            categories = Category.objects.filter(Q(category_name__icontains=keyword)|Q(description__icontains=keyword))
            print(categories)
            

            
            
    context = {
        'products':products ,
        'categories': categories,
    }
    return render(request,"admin_dashboard/page-products-list.html",context)
