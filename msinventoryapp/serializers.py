from rest_framework import serializers
from .models import (
    Product, PriorityLevel, ProductCategory, FavoriteType, 
    Company, ProductType, PurchaseOrderStatusType, Location,
    PurchaseOrder, StockMoveType, StockMove, InventoryLevel
)
# pylint: disable=all

class ProductSerializer(serializers.ModelSerializer):
    favorite_name = serializers.CharField(source="favorite.name", read_only=True)
    product_category_name = serializers.CharField(source="product_category.name", read_only=True)
    product_type_name = serializers.CharField(source="product_type.name", read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'favorite', 'favorite_name',
            'name',
            'internal_reference',
            'barcode',
            'sales_price',
            'cost',
            'product_category', 'product_category_name',
            'product_type', 'product_type_name',
            'quantity_on_hand',
            'forecasted_quantity'
        ]

class PriorityLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriorityLevel
        fields = [
            'id',
            'name', 
            'description'
        ]
        
class FavoriteTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriorityLevel
        fields = [
            'id',
            'name', 
            'description',
            'color'
        ]
        
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = [
            'id',
            'name', 
            'parent',
            'full_path'
        ]

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'id',
            'name', 
            'is_company',
            'related_company',
            'street',
            'zip_code',
            'city',
            'state',
            'country',
        ]
        
class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'id',
            'description', 
        ]
class PurchaseOrderStatusTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'id',
            'name',
            'description', 
        ]

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'id',
            'code',
            'name',
            'description', 
        ]
        
class PriorityLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriorityLevel
        fields = [
            'id',
            'name', 
            'description'
        ]

class FavoriteTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteType
        fields = [
            'id',
            'name', 
            'description',
            'color'
        ]

class ProductCategorySerializer(serializers.ModelSerializer):
    parent_name = serializers.CharField(source='parent.name', read_only=True)
    
    class Meta:
        model = ProductCategory
        fields = [
            'id',
            'name', 
            'parent',
            'parent_name',
            'full_path'
        ]

class CompanySerializer(serializers.ModelSerializer):
    related_company_name = serializers.CharField(source='related_company.name', read_only=True)
    
    class Meta:
        model = Company
        fields = [
            'id',
            'name', 
            'is_company',
            'related_company',
            'related_company_name',
            'street',
            'zip_code',
            'city',
            'state',
            'country',
        ]

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = [
            'id',
            'name',
            'description', 
        ]

class PurchaseOrderStatusTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderStatusType
        fields = [
            'id',
            'name',
            'description', 
        ]

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = [
            'id',
            'code',
            'name',
            'description', 
        ]

class ProductSerializer(serializers.ModelSerializer):
    favorite_name = serializers.CharField(source="favorite.name", read_only=True)
    product_category_name = serializers.CharField(source="product_category.name", read_only=True)
    product_type_name = serializers.CharField(source="product_type.name", read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'favorite', 'favorite_name',
            'name',
            'internal_reference',
            'responsible',
            'barcode',
            'sales_price',
            'cost',
            'product_category', 'product_category_name',
            'product_type', 'product_type_name',
            'quantity_on_hand',
            'forecasted_quantity',
            'activity_exception_decoration'
        ]

class PurchaseOrderSerializer(serializers.ModelSerializer):
    priority_name = serializers.CharField(source='priority.name', read_only=True)
    vendor_name = serializers.CharField(source='vendor.name', read_only=True)
    status_name = serializers.CharField(source='status.name', read_only=True)
    
    class Meta:
        model = PurchaseOrder
        fields = [
            'id',
            'priority', 'priority_name',
            'order_reference',
            'vendor', 'vendor_name',
            'purchase_representative',
            'order_deadline',
            'activities',
            'source_document',
            'total',
            'status', 'status_name'
        ]

class StockMoveTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockMoveType
        fields = [
            'id',
            'name',
            'code'
        ]

class StockMoveSerializer(serializers.ModelSerializer):
    move_type_name = serializers.CharField(source='move_type.name', read_only=True)
    move_type_code = serializers.CharField(source='move_type.code', read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)
    from_location_name = serializers.CharField(source='from_location.name', read_only=True)
    from_location_code = serializers.CharField(source='from_location.code', read_only=True)
    to_location_name = serializers.CharField(source='to_location.name', read_only=True)
    to_location_code = serializers.CharField(source='to_location.code', read_only=True)
    
    class Meta:
        model = StockMove
        fields = [
            'id',
            'move_type', 'move_type_name', 'move_type_code',
            'product', 'product_name',
            'quantity',
            'from_location', 'from_location_name', 'from_location_code',
            'to_location', 'to_location_name', 'to_location_code',
            'timestamp',
            'description'
        ]

class InventoryLevelSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_internal_reference = serializers.CharField(source='product.internal_reference', read_only=True)
    location_name = serializers.CharField(source='location.name', read_only=True)
    location_code = serializers.CharField(source='location.code', read_only=True)
    
    class Meta:
        model = InventoryLevel
        fields = [
            'id',
            'product', 'product_name', 'product_internal_reference',
            'location', 'location_name', 'location_code',
            'quantity',
            'last_updated'
        ]