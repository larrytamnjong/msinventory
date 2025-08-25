
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets
from .models import (
    Product, PriorityLevel, ProductCategory, FavoriteType, 
    Company, ProductType, PurchaseOrderStatusType, Location,
    PurchaseOrder, StockMoveType, StockMove, InventoryLevel
)
from .serializers import (
    ProductSerializer, PriorityLevelSerializer, ProductCategorySerializer, 
    FavoriteTypeSerializer, CompanySerializer, ProductTypeSerializer,
    PurchaseOrderStatusTypeSerializer, LocationSerializer, PurchaseOrderSerializer,
    StockMoveTypeSerializer, StockMoveSerializer, InventoryLevelSerializer
)
# pylint: disable=all

class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return Response({"message": "Welcome to the Inventory Management System API"})

class PriorityLevelViewSet(viewsets.ModelViewSet):
    queryset = PriorityLevel.objects.all()
    serializer_class = PriorityLevelSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class FavoriteTypeViewSet(viewsets.ModelViewSet):
    queryset = FavoriteType.objects.all()
    serializer_class = FavoriteTypeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class PurchaseOrderStatusTypeViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrderStatusType.objects.all()
    serializer_class = PurchaseOrderStatusTypeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class StockMoveTypeViewSet(viewsets.ModelViewSet):
    queryset = StockMoveType.objects.all()
    serializer_class = StockMoveTypeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class StockMoveViewSet(viewsets.ModelViewSet):
    queryset = StockMove.objects.all()
    serializer_class = StockMoveSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class InventoryLevelViewSet(viewsets.ModelViewSet):
    queryset = InventoryLevel.objects.all()
    serializer_class = InventoryLevelSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]