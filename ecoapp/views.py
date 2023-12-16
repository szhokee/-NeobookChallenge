from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.apps import apps
from django.shortcuts import redirect
from .models import Category, Product, CartItem, Order
from .serializers import CategorySerializer, ProductSerializer, CartItemSerializer, OrderSerializer


class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        CategorySerializer = apps.get_model('ecoapp', 'CategorySerializer')
        serializer = CategorySerializer(categories, many=True)
        return Response({"categories": serializer.data})


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({"products": serializer.data})


class CartView(APIView):
    def get(self, request):
        cart_items = CartItem.objects.all()
        serializer = CartItemSerializer(cart_items, many=True)
        total_price = sum(item.total_price() for item in cart_items)
        return Response({"cart": serializer.data, "total_price": total_price})

    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        # Логика для обновления количества товара в корзине
        pass

    def delete(self, request, product_id):
        # Логика для удаления товара из корзины
        pass


class ProductDetailView(APIView):
    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class OrderSuccessView(APIView):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        return Response({"order_id": order.id, "timestamp": order.timestamp})
    

class OrderView(APIView):
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            # Перенаправьте пользователя на страницу успешного заказа с номером заказа
            return redirect('order-success', order_id=order.id)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderHistoryView(APIView):
    def get(self, request):
        orders = Order.objects.all().order_by('-timestamp')  # Сортировка по дате в убывающем порядке
        serializer = OrderSerializer(orders, many=True)
        return Response({"orders": serializer.data})

class OrderDetailsView(APIView):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        serializer = OrderSerializer(order)
        return Response({"order": serializer.data})