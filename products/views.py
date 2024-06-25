from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(stock=100)

class UpdateStockView(APIView):
    def patch(self, request, pk, format=None):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        stock_increment = request.data.get('stock', 0)
        product.stock += stock_increment
        product.save()

        if product.stock < 10:
            print(f"ALERT: The stock for product {product.name} is below 10.")

        return Response(ProductSerializer(product).data, status=status.HTTP_200_OK)

class OrderCreateView(APIView):
    def post(self, request, format=None):
        # Dummy implementation for creating orders and reducing stock
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)
        
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if product.stock < quantity:
            return Response({"error": "Insufficient stock"}, status=status.HTTP_400_BAD_REQUEST)
        
        product.stock -= quantity
        product.save()
        
        if product.stock < 10:
            print(f"ALERT: The stock for product {product.name} is below 10.")
        
        return Response(ProductSerializer(product).data, status=status.HTTP_200_OK)
