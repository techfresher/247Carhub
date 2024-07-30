from django.db import models
from datetime import datetime

class Contact(models.Model):
    user_id = models.IntegerField(blank=True)
    car_id = models.IntegerField()
    car_title = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    customer_need = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    create_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email
