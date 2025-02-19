from django.contrib.auth.models import User
from django.db import models

class Order(models.Model):

    NEW = 'Nowy'
    CONTACTED = 'Zlecenie przyjęte'
    INPROGRESS = 'W realizacji'
    FINISH = 'Ukończone zlecenie'
    STARTERMOTOR = 'Rozrusznik'
    ALTERNATOR = 'Alternator'
    
    CHOICES_ITEM = (
        (STARTERMOTOR, 'Rozrusznik'),
        (ALTERNATOR, 'Alternator')
    )

    CHOICES_STATUS = (
        (NEW, 'Nowy'),
        (CONTACTED, 'Zlecenie przyjęte'),
        (INPROGRESS, 'W realizacji'),
        (FINISH, 'Ukończone zlecenie'),
    )

    item = models.CharField(max_length=15, choices=CHOICES_ITEM)
    car_name = models.CharField(max_length=255)
    car_model = models.CharField(max_length=255)
    car_engine = models.CharField(max_length=255)
    car_vin = models.CharField(max_length=17)
    item_number = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=25, choices=CHOICES_STATUS, default=NEW)
    created_by = models.ForeignKey(User,related_name='orders', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    