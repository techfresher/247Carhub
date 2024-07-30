from django.contrib import admin
from .models import car
from django.utils.html import format_html
# Register your models here.
class carAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50px;" />'.format(object.car_photo.url))

    thumbnail.short_description = "car image"
    list_display = ('id', 'thumbnail', 'car_title', 'color', 'year', 'city', 'is_feature')
    list_display_links = ('id', 'thumbnail','car_title')
    list_editable = ('is_feature',)
    search_fields = ('id', 'city', 'state',)
    list_filter = ('state', 'fuel_type', 'color', 'transission')
admin.site.register(car, carAdmin)