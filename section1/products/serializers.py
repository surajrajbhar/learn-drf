from rest_framework import serializers
from .models import Products , Manufacturers

class product_serializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class manufacturer_serializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturers
        fields  = '__all__'

