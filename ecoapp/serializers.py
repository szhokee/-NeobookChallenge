from rest_framework import serializers
from .models import Category, Product, CartItem, Order
from django.apps import apps

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image_url']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'image_url', 'price_per_unit', 'description']

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price_per_unit', 'image_url', 'description']

class CartItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product_id', 'quantity']

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = CartItemDetailSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'name', 'phone', 'address', 'items', 'total_price']
