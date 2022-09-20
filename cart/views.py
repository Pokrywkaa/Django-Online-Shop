from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from shop.models import Product
from .cart import Cart
from .serializers import CartAddSerializer

class CartView(APIView):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        serializer = CartAddSerializer(data=request.data)
        if serializer.is_valid():
            cd = serializer.data
            cart.add(product=product,
                    quantity=cd['quantity'],
                    override_quantity=cd['override'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)