from django.shortcuts import render, get_object_or_404
from .models import car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
def cars(request):
    cars = car.objects.order_by('-created_date')
    paginator = Paginator(cars, 2)
    page = request.GET.get('page')
    car_pages = paginator.get_page(page)
    model_search = car.objects.values_list('model', flat=True).distinct()
    city_search = car.objects.values_list('city', flat=True).distinct()
    year_search = car.objects.values_list('year', flat=True).distinct()
    body_style_search = car.objects.values_list('body_style', flat=True).distinct
    data = {
        "cars":car_pages, 
        'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style_search':body_style_search
    }
    return render(request, 'cars/cars.html', data)

def car_detail(request, id):
    single_car = get_object_or_404(car, pk=id)
    data = { 
        'single_car':single_car
    }
    return render(request, 'cars/car_detail.html', data)


def search(request):
    model_search = car.objects.values_list('model', flat=True).distinct()
    city_search = car.objects.values_list('city', flat=True).distinct()
    year_search = car.objects.values_list('year', flat=True).distinct()
    body_style_search = car.objects.values_list('body_style', flat=True).distinct
    transission_search = car.objects.values_list('transission', flat=True).distinct
    cars = car.objects.order_by('-created_date')
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            cars = cars.filter(price__iexact=price)

    if '' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)                

    data = {
        "cars":cars,
         'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style_search':body_style_search,
        'transission_search':transission_search,
    }
    return render(request, 'cars/search.html', data)