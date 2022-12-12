from django.shortcuts import render,redirect
from rest_framework import generics
from .models import *
# from .API.serializers import plans_serializer
from wallet_and_money.models import *
from recharge_plans.models import *
from .API.serializers import *
# Create your views here.


def recharge_number(request,*args,**kwargs):
    plan_id = kwargs.get('plan_id')
    phn_no  = kwargs.get('phone_no',)
    user = request.user
    wallet_money = Wallet.objects.get(Wallet_of=user)
    plan = plans.objects.get(plan_id=plan_id)
    orderid:str
    if(plan.price <= wallet_money.Balance):
        order=recharge_record.objects.create(recharged_by=user,plan=plan,phone_number=phn_no,recharged_status='Success')
        order.save()
        orderid=order.order_id
        Wallet.objects.filter(Wallet_of=user).update(Balance=wallet_money.Balance-plan.price)
        
    elif(plan.price > wallet_money.Balance):
        order=recharge_record.objects.create(recharged_by=user,plan=plan,phone_number=phn_no,recharged_status='Failed')
        order.save()
        orderid=order.order_id
    else:
        order=recharge_record.objects.create(recharged_by=user,plan=plan,phone_number=phn_no,recharged_status='Processing')
        order.save()
        orderid=order.order_id
    
    return redirect(f'/recharge/api/response/{orderid}/')


class recharge_response(generics.ListAPIView):
    serializer_class = recharge_record_serializer
    
    def get_queryset(self):
        order_id = self.kwargs.get('order_id')
        return recharge_record.objects.filter(order_id=order_id)