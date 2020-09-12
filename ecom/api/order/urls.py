from rest_framework import routers
from django.urls import path, include
from . import views


router = routers.DefaultRouter()
router.register(r'', views.OrderViewSet)

urlpatterns = [
    path('add/<str:_id>/<str:token>/', views.add, name="order_add"),
    path('', include(router.urls))
]
