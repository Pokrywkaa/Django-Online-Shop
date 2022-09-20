from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>/', views.CartView.as_view(), name='cart_add'),
]