from rest_framework import serializers

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()
    override = serializers.BooleanField(required=False,
                            initial=False)