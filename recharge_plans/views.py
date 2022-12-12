from rest_framework import generics
from .models import *
from .API.serializers import plans_serializer

class plans_operator_name(generics.ListAPIView):
    # queryset = plans.objects.all()
    serializer_class = plans_serializer
    
    def get_queryset(self):
        operator= self.kwargs['network_operator']
        return plans.objects.filter(Netowrk_operator=operator)
    
class plans_operator_name_location(generics.ListAPIView):
    serializer_class = plans_serializer
    
    def get_queryset(self):
        operator= self.kwargs['network_operator']
        location = self.kwargs['location']
        return plans.objects.filter(Netowrk_operator=operator,locality=location)