from rest_framework import serializers
from .models import Category, Product, CartItem, Order
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.apps import apps
from .models import Category, Product, CartItem, Order
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    CartItemSerializer,
    OrderSerializer
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image_url']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'image_url', 'price_per_unit']

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']

    def to_representation(self, instance):
        ProductSerializer = apps.get_model('ecoapp', 'ProductSerializer')
        product_serializer = ProductSerializer()
        return {
            'id': instance.id,
            'product': product_serializer.to_representation(instance.product),
            'quantity': instance.quantity
        }
    
class OrderSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'name', 'phone', 'address', 'items', 'total_price']
