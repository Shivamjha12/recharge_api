from django.db import models
import uuid
from Accounts.models import * 
from recharge_plans.models import *
# Create your models here.

status=(
    ('Processing','PROCESSING'),
    ('Success','SUCCESS'),
    ('Failed','FAILED'),
)

class recharge_record(models.Model):
    recharged_by     = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    plan             = models.ForeignKey(plans,on_delete=models.CASCADE)
    phone_number     = models.CharField(max_length=10,blank=True,null=True)
    date             = models.DateTimeField(auto_now_add=True)
    order_id         = models.UUIDField(default=uuid.uuid4, editable=False)
    recharged_status = models.CharField(max_length=30,choices=status)
    
    def __str__(self):
        return str(self.recharged_by) + " recharge on " + str(self.date)[:-21] + " and order id is "+ str(self.order_id)
    