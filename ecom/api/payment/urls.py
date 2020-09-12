from django.urls import path
from . import views


urlpatterns = [
    path('gettoken/<str:_id>/<str:token>/', views.generate_token, name="payment_generate_token"),
    path('process/<str:_id>/<str:token>/', views.process_payment, name="payment_process"),
]
