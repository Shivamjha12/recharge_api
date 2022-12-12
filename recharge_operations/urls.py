from django.urls import path,include
from recharge_operations import views

urlpatterns = [
    path('api/<str:plan_id>/<int:phone_no>/', views.recharge_number, name='rechage_number'),
    path('api/response/<str:order_id>/', views.recharge_response.as_view(), name='recharge_response'),
]
