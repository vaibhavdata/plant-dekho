from django.shortcuts import render, redirect
from django.contrib import messages
from nursery_ecommerce_app.models.customer import Contact
from django.core.mail import send_mail
from accounts.models import Account
from django.conf import settings
# Create your views here.
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        customer_need = request.POST['customer_need']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        
        email_subject = 'You have a new message from plates dekho website regarding ' + customer_need
        message_body = 'Name: ' + name + '. Email: ' + email + '. Phone: ' + phone + '. Message: ' + message

        admin_info = Account.objects.get(is_admin=True)
        admin_email = admin_info.email
        send_mail(
                email_subject,
                message_body,
                'testkro356@gmail.com',
                [admin_email],
                fail_silently=False,
            )
        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('contact')
        
    return render(request,"contact.html")
