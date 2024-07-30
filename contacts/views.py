from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings

def inquiry(request):
    if request.method == "POST":
        # Collecting data from the POST request using .get method
        user_id = request.POST.get('user_id')
        car_title = request.POST.get('car_title')
        car_id = request.POST.get('car_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        customer_need = request.POST.get('customer_need')
        city = request.POST.get('city')
        state = request.POST.get('state')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
            
        if request.user.is_authenticated:
            user_id = request.user.id
            inquired = Contact.objects.all().filter(car_id=car_id, user_id = user_id)
            if inquired:
                messages.error(request, 'you already make inquiry about this car, please wait for a response from us')
                return redirect('/cars/' + car_id)
                    
        # saving conotact
        contact = Contact(
            user_id=user_id,
            car_title=car_title,
            car_id=car_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            customer_need=customer_need,
            city=city,
            state=state,
            phone_number=phone_number,
            message=message
        )

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            "New Car Inquiry",
            "you have a new car inquiry." + car_title + 'please login for more information about the buyer.',
            "joshuasundayola@gmail.com",
            [admin_email],
            fail_silently=False,
)

        contact.save()
        messages.success(request, 'You have successfully submitted, we will get back to you soon.')
        return redirect('/cars/' + car_id)
    return redirect('/')
