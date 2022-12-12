from django.urls import path,include
from .views import *

urlpatterns = [
    path('api/<str:network_operator>/',plans_operator_name.as_view()),
    path('api/<str:network_operator>/<str:location>/',plans_operator_name_location.as_view()),
]
# <str:network_operator>
