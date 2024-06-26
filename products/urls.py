from django.urls import path, register_converter
from .views import ProductCreateView, UpdateStockView, OrderCreateView
from django.urls.converters import UUIDConverter


urlpatterns = [
    path("", ProductCreateView.as_view(), name="product-create"),
    path("products", ProductCreateView.as_view(), name="product-create"),
    path(
        "inventories/product/<str:pk>", UpdateStockView.as_view(), name="update-stock"
    ),
    path("orders", OrderCreateView.as_view(), name="order-create"),
]
