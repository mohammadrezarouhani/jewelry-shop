from ast import Delete
from rest_framework import serializers
from .models import Factor, Product, FactorProduct
import pdb 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'


class ProductSoldSerializer(serializers.ModelSerializer):
    class Meta:
        model=FactorProduct
        fields=['id','product','name','price','number']


class FactorSerializer(serializers.ModelSerializer):
    product_sold=ProductSoldSerializer(many=True)

    class Meta:
        model=Factor
        fields=['id','seller','customer_name',
                'payment_type','total_price','tax',
                'discount','comment','date',"product_sold"]

    def create(self, validated_data):
        product=validated_data.pop('product_sold')
        factor=Factor.objects.create(**validated_data)

        for data in product:
            FactorProduct.objects.create(**data,factor=factor)
        return factor


    def update(self, instance, validated_data):
        product=validated_data.pop("product_sold")
        FactorProduct.objects.filter(factor=instance).delete()

        for data in product:
            FactorProduct.objects.create(**data,factor=instance)

        return super().update(instance,validated_data)


    