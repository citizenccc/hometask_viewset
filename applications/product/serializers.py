from rest_framework import serializers

from applications.product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')

    def create(self, validated_data):
        product = Product.objects.create(**validated_data)
        return product


