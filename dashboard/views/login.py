from email.mime import message
from multiprocessing import context
from accounts.views import edit_profile
from dashboard.froms.admin_form import AdminForm, AdminProfileForm, AdminRegistrationForm
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages, auth
from accounts.models import Account,UserProfile
from django.contrib.auth.decorators import login_required

# Create your views here.
def admin_register(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        print(form)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            admin = Account.objects.createSuperUser(first_name=first_name, last_name=last_name, email=email, username=username,password=password)
            admin.phone_number = phone_number
            admin.save()

            # Create a user profile
            #profile = UserProfile()
            #profile.user_id = user.id
            #profile.profile_picture = 'default/default-user.png'
            #profile.save()

            # USER ACTIVATION
            
            messages.success(request, 'Your login Admin of project ')
            return redirect("admin_dashboard")
    else:
        form = AdminRegistrationForm()
    context = {
        'form': form,
    }
    
    return render(request, 'admin_dashboard/page-account-register.html',context)
def admin_login(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now admin logged in.')
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('admin_login')
    return render(request, 'admin_dashboard/page-account-login.html')
@login_required(login_url='admin_login')
def admin_logout(request):
    url = request.META.get('HTTP_REFERER')
    if request.user.is_admin:
        auth.logout(request)
        messages.success(request,'You are logout succesfully')
        return redirect('admin_login')
    else:
        messages.success(request,"logout only admin ")
        return redirect(url)
def admin_edit_profile(request):
    adminprofile = UserProfile.objects.filter(user= request.user)
    if request.method =="POST":
        admin_form = AdminForm(request.POST,instance =request.user)
        profile_Form = AdminProfileForm(request.POST,request.FILES,instance =adminprofile)
        if admin_form.is_valid() and profile_Form.is_valid():
            admin_form.save()
            profile_Form.save()
            messages.success(request,"Admin profile update")
            return redirect('admin_edit_profile')
    else:
        admin_form = AdminForm()
        profile_Form = AdminProfileForm()
    context ={
        'admin_form':admin_form,
        'profile_Form':profile_Form,
    }
    return render(request,"admin_dashboard/profile_settings.html",context)

    
