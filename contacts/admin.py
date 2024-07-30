from django.contrib import admin
from .models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'city', 'state', 'email', 'car_title', 'create_date', 'phone_number')
    list_display_links = ('id', 'first_name', 'last_name', 'car_title')
    list_per_page = 25
    search_fields = ('first_name', 'last_name', 'car_title', 'email')



admin.site.register(Contact)

