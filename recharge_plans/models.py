from django.db import models
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
locations= (
    ('Delhi', 'DELHI'),
    ('Delhi_ncr','DELHI NCR'),
    ('Mumbai','MUMBAI'),
    ('Kolkata','Kolkata'),
    ('Banglore','Banglore'), 
)

netowrk_operator=(
    ('Airtel','AIRTEL'),
    ('Jio','JIO'),
    ('Idea','IDEA'),
    ('Vodafone','VODAFONE'),
    ('Bsnl','BSNL'),
)

"""
--> Why i create plan model <--
If we have api for getting plans of network operator the we use it directly, 
but if we don't have api's then we have no other choices then
1) we scrap the data from other website but it is not efficient
2) we can create our own plans model to do recharge

"""

class plans(models.Model):
    plan_id            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Netowrk_operator   = models.CharField(max_length=30,choices=netowrk_operator)
    locality           = models.CharField(max_length=100,default="",blank=True,choices=locations)
    price= models.IntegerField(
                         validators=[MaxValueValidator(10000),MinValueValidator(10)],
                         blank=True,null=True
                        )
    # taking validity as no of days 
    validity           = models.IntegerField(
                         validators=[MaxValueValidator(365),MinValueValidator(1)],
                         blank=True,null=True
                         )
    plan_creating_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.Netowrk_operator +" "+str(self.plan_id)
    @property
    def plan_price(self):
        return self.price
    