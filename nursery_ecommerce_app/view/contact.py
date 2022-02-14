from django.shortcuts import render, redirect
from django.contrib import messages
from nursery_ecommerce_app.models.customer import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings
# Create your views here.
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        customer_need = request.POST.get('customer_need')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contact = Contact(name=name, customer_need=customer_need, email=email, phone=phone, message=message)
        #admin_info = User.objects.get(is_superuser=True)
        #admin_email = admin_info.email
        email_subject = 'You have a new message from plates dekho website regarding ' + customer_need
        message_body = 'Name: ' + name + '. Email: ' + email + '. Phone: ' + phone + '. Message: ' + message
        send_mail(
                email_subject,
                message_body,
                settings.EMAIL_HOST_USER,
		        ['vaibhavmc01@gmail.com'], 
                fail_silently=False,
        )

        contact.save()
        messages.success(request, 'Your request has been submitted, we will get back to you shortly.')
        return redirect("contact")
    
    return render(request,"contact.html")