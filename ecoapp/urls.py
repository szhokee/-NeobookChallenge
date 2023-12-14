from django.urls import path
from django.urls import path
from .views import YourMainView
from .views import CategoryListView, ProductListView, CartView, OrderView

urlpatterns = [
    # Эндпоинты для категорий и товаров
    path('your-main-view/', YourMainView.as_view(), name='your-main-view'),
    path('api/categories/', CategoryListView.as_view(), name='category-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('api/products/<int:category_id>/', ProductListView.as_view(), name='product-list'),

    # Эндпоинты для корзины
    path('api/cart/', CartView.as_view(), name='cart-detail'),
    path('api/cart/add/', CartView.as_view(), name='cart-add'),
    path('api/cart/update/', CartView.as_view(), name='cart-update'),
    path('api/cart/remove/<int:product_id>/', CartView.as_view(), name='cart-remove'),

    # Эндпоинт для оформления заказа
    path('api/order/place/', OrderView.as_view(), name='order-place'),
]
