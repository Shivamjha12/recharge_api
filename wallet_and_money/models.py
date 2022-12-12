from django.db import models
from Accounts.models import *
from django.core.validators import MaxValueValidator,MinValueValidator
import uuid
# Create your models here.

class Wallet(models.Model):
    Wallet_of         = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    Balance           = models.IntegerField(
                         validators=[MaxValueValidator(150000),MinValueValidator(0)],
                         blank=True,null=True
                        )
    wallet_adress     = models.UUIDField(default=uuid.uuid4, editable=False)
    wallet_created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'The wallet adress of {self.Wallet_of} wallet is {self.wallet_adress}'
    
    @property
    def wallet_balance(self):
        return self.Balance