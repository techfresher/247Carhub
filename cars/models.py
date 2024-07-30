from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField 
from multiselectfield import MultiSelectField
# Create your models here.
class car(models.Model):
    state_choice = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('LA', 'Lagos'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OS', 'OSun'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r,r))

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )
    transission_choice = (
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual'),
    )
    # door_choices = (
    #     ('2', '2'),
    #     ('3', '3'),
    #     ('4', '4'),
    #     ('5', '5'),
    #     ('6', '6'),
    # )

    condition_choice = (
        ('New', 'New'),
        ('used', 'used'),
    )

    car_title = models.CharField(max_length=100)
    state = models.CharField(choices=state_choice, max_length=50)
    city = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    condition = models.CharField(choices=condition_choice, max_length=100)
    year = models.IntegerField(('year'),choices=year_choice)
    price = models.IntegerField()
    description = RichTextField()
    color = models.CharField(max_length=50)
    car_photo = models.ImageField(upload_to="photo/%Y/%m/%d/")
    car_photo_1 = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True)
    car_photo_2 = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True)
    car_photo_3 = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True)
    car_photo_4 = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True)
    feature = MultiSelectField(choices=features_choices, max_length=250)
    body_style = models.CharField(max_length=150)
    transission = models.CharField(choices=transission_choice, max_length=150)
    minage = models.IntegerField()
    doors = models.IntegerField()
    miles = models.IntegerField()
    interior = models.CharField(max_length=150)
    passager = models.IntegerField()
    engine = models.CharField(max_length=100)
    vin_no = models.CharField(max_length=150)
    no_of_owners = models.IntegerField()
    fuel_type = models.CharField(max_length=150)
    is_feature = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now,blank=True)
    
    def __str__(self):
        return self.car_title