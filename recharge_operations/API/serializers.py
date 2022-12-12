from rest_framework import serializers
from recharge_operations.models import *

class recharge_record_serializer(serializers.ModelSerializer):
    class Meta:
        fields = ('recharged_by','plan','phone_number','date','order_id','recharged_status')
        model  = recharge_record