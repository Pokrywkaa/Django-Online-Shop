from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class ProductList(APIView):
    def get(self, request, category_slug=None):
        category = None
        categories = Category.objects.all()
        products = Product.objects.filter(available=True)
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)
        serializer = ProductSerializer(products, many=True, context={"request":request})
        return Response(serializer.data)

class ProductDetail(APIView):
    def get(self, request, id, slug):
        product = get_object_or_404(Product,
                                    id=id,
                                    slug=slug,
                                    available=True)
        serializer = ProductSerializer(product, context={"request":request})
        return Response(serializer.data)
