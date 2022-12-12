from rest_framework import serializers
from  recharge_plans.models import *
class plans_serializer(serializers.ModelSerializer):
    class Meta:
        fields = ('price','locality','description','validity')
        model  = plans