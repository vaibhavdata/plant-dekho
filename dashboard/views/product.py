from sys import implementation
from django.shortcuts import render,redirect,get_object_or_404
from nursery_ecommerce_app.models.product import Product
from nursery_ecommerce_app.models.category import Category
from dashboard.froms.product_from import ProductForm
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse

def admin_form_product(request):
    return render(request,"admin_dashboard/page-form-product-1.html")

def admin_product_grid(request):
    return render(request,"admin_dashboard/page-products-grid.html")
def admin_product_add(request,product_id):
    product = get_object_or_404(Product, product_id=product_id)
    url = request.META.get('HTTP_REFERER')
   #return HttpResponse(url)
    if request.method == 'POST':  # check post
        form = ProductForm(request.POST)
        if form.is_valid():
            data = Product()
            print(data)
            data.product_name= form.cleaned_data['product_name']
            data.slug = form.cleaned_data['slug']
            data.description = form.cleaned_data['description']
            data.price = form.cleaned_data['price']
            data.images = form.cleaned_data['images']
            data.stock = form.cleaned_data['stock']
            data.label = form.cleaned_data['label']
            data.category = form.cleaned_data['category']
            data.is_available = form.cleaned_data['is_available']
            data.product_id = product_id
            #data.user_id = request.user.id
            data.save()
            messages.success(request, 'Thank you! Your review has been submitted.')
            return redirect(url)
        return render(request,"admin_dashboard/product_add.html")
    '''if request.method == 'POST':
        product_name = request.POST.get('product_name')
        slug = request.POST.get('slug')
        description = request.POST.get('description')
        price = request.POST.get('price')
        images = request.POST.get('images')
        stock = request.POST.get('stock')
        label = request.POST.get('label')
        category =Category.objects.get(pk='id')
        #category = request.POST.get('category')
        data = Product(product_name=product_name,slug=slug,description=description,price=price,images=images,stock=stock,label=label,category=category)
        data.save()
        messages.success(request, 'Your request has been submitted, we will get back to you shortly.')
        return redirect("admin_product_add")
    
    return render(request,"admin_dashboard/product_add.html")'''

        


def admin_add_product_view(request):
    productForm=ProductForm()
    if request.method=='POST':
        products = Product.objects.get()
        #product=Product.objects.get(product_id =product_id)
        productForm=ProductForm(request.POST, request.FILES,instance=products)
        if productForm.is_valid():
            productForm.save()
            print(ProductForm)
        return HttpResponseRedirect('admin_product_list')
    return render(request,'admin_dashboard/product_add.html',{'productForm':productForm})

# reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
def admin_products_list(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
        
        

    context = {
        'products': paged_products,
        'product_count': product_count,
    }
    return render(request,"admin_dashboard/page-products-list.html",context)

