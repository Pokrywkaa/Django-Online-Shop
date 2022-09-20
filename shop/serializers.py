from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None,
                                        allow_null=True,
                                        required=False)
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = '__all__'


