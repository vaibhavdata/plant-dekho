from django.shortcuts import render,HttpResponseRedirect,get_object_or_404
from nursery_ecommerce_app.models.category import Category
from nursery_ecommerce_app.models.product import Product,ReviewRating


def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('created_date')
    categories = Category.objects.all()[:6]
    #products_slider = Product.objects.all().order_by('id')[:4]  #first 4 products
    products_picked = Product.objects.all().order_by('?')[:4] # randomly select product
    products_latest = Product.objects.all().order_by('-id')[:4]  # last 4 products
    category_latest = Category.objects.all().order_by('-id')[:5] 
    # Get the reviews
    reviews = None
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': products,
        'reviews': reviews,
        'categories' : categories,
        'products_picked' : products_picked,
        #'products_slider' : products_slider,
        'products_latest' : products_latest,
        'category_latest' : category_latest,

    }
    return render(request, 'home.html', context)



