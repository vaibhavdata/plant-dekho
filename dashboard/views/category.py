from unicodedata import category
from django.shortcuts import redirect, render,get_object_or_404
from nursery_ecommerce_app.models.category import Category
from nursery_ecommerce_app.models.product import Product
from dashboard.froms.category_form import CategoryForm
from django.http import HttpResponseRedirect,HttpResponse
def admin_products_category(request):
    categories=Category.objects.all()
    context = {
        'categories':categories,
    }

    return render(request,"admin_dashboard/page-categories.html",context)
def admin_add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST,request.FILES)
        
        if form.is_valid():
            data = Category()
            data.category_name =form.cleaned_data['category_name']
            data.slug = form.cleaned_data['slug']
            data.description = form.cleaned_data['description']
            data.cat_image = form.cleaned_data['cat_image']
            
            data.save()
           
            request.session['success'] = "Successfully added category"
            return redirect('admin_products_category')
        else:
            return redirect("admin_add_category")
    return render(request,"admin_dashboard/admin_add_category.html")
def admin_edit_category(request,category_slug):
    categories = Category.objects.get(slug=category_slug)
    print(categories)
    categoryForm=CategoryForm(instance=categories )
    if request.method=='POST':
        categoryForm=CategoryForm(request.POST,request.FILES,instance=categoryForm)
        if CategoryForm.is_valid():
            CategoryForm.save()
            return redirect('admin_products_category')
    return render(request,"admin_dashboard/admin_edit_category.html")
            
   

        
    

    