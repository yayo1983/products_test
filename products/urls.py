from django.urls import path
from .views import ProductCreateView, UpdateStockView, OrderCreateView

urlpatterns = [
    path("", ProductCreateView.as_view(), name="product-create"),
    path("products", ProductCreateView.as_view(), name="product-create"),
    path(
        "inventories/product/<int:pk>", UpdateStockView.as_view(), name="update-stock"
    ),
    path("orders", OrderCreateView.as_view(), name="order-create"),
]
