from django.shortcuts import render, redirect
from .models import Team
from cars.models import car
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_car = car.objects.order_by('-created_date').filter(is_feature=True)
    all_cars = car.objects.order_by('-created_date')
    model_search = car.objects.values_list('model', flat=True).distinct()
    city_search = car.objects.values_list('city', flat=True).distinct()
    year_search = car.objects.values_list('year', flat=True).distinct()
    body_style_search = car.objects.values_list('body_style', flat=True).distinct
    data = {
        'teams':teams, 
        'featured_car':featured_car,
        'all_cars':all_cars,
        'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style_search':body_style_search
        
    }
    return render(request, 'pages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams':teams
    }
    return render(request, 'pages/about.html', data)

def service(request):
    return render(request, 'pages/service.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        email_subject = 'you have a new message from carzone regarding' + subject
        message_body = 'Name: '+name+'.Email:'+email+'.phone: '+phone+'.message:'+message
        send_mail(
            email_subject, 
            message_body,
            'joshuasundayola@gmail.com',
            [admin_email],
            fail_silently=False,
        )
        messages.success(request, 'thank you for contacting us, we will get back to you shortly.')
        return redirect('contact')
    return render(request, 'pages/contact.html')