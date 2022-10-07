from django.urls import path
from . import views


app_name = 'order'
urlpatterns = [
    path('', views.Payment.as_view(), name='payment'),
    path('concludeorder/', views.ConcludeOrder.as_view(), name='concludeorder'),
    path('orderdetail/', views.OrderDetail.as_view(), name='orderdetail'),
]
