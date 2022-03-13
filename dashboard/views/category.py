from email import message
from pyexpat.errors import messages
from unicodedata import category
from django.shortcuts import redirect, render,get_object_or_404
from nursery_ecommerce_app.models.category import Category
from nursery_ecommerce_app.models.product import Product
from dashboard.froms.category_form import CategoryForm
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
@login_required(login_url='admin_login')
def admin_products_category(request):
    categories=Category.objects.all()
    context = {
        'categories':categories,
    }
    

    return render(request,"admin_dashboard/page-categories.html",context)
@login_required(login_url='admin_login')
def admin_add_category(request):
    context = {}
    if request.method == 'POST':
        form = CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            data = Category()
            category_name = form.cleaned_data.get('category_name')
            slug = form.cleaned_data.get('slug')
            description = form.cleaned_data.get('description')
            cat_image = form.cleaned_data.get('cat_image')
            obj  = Category.objects.create(category_name=category_name,slug=slug,description=description,cat_image=cat_image)
            obj.save()
            return redirect('admin_products_category')
        
        else:
            form = CategoryForm()
            context['form']= form
            return redirect("admin_add_category")
    return render(request,"admin_dashboard/admin_add_category.html",context)
@login_required(login_url='admin_login')
def admin_delete_category(request,category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect('admin_products_category')
@login_required(login_url='admin_login')
def admin_edit_category(request,category_id):
    category = get_object_or_404(Category,id=category_id)
    if request.method =="POST":
        form = CategoryForm(request.POST,request.FILES,instance=category)
        if form.is_valid():
            
            
            category = form.save(commit=False)
            category.save()
            
            return redirect(reverse('admin_products_category'))
            
    else:
        form = CategoryForm(instance=category)
    context = {'form':form}
    return render(request,"admin_dashboard/admin_edit_category.html",context)
@login_required(login_url='admin_login')
def category_search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            categories = Category.objects.filter(Q(category_name__icontains=keyword)|Q(description__icontains=keyword))
            category_count = categories.count()

    context = {
        
        'category_count': category_count,
        'categories': categories,
    }
    return render(request,"admin_dashboard/page-categories.html",context)
        


            
   

        
    

    