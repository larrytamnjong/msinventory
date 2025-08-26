from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# pylint: disable=all

# Priority levels for various entities
class PriorityLevel(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return str(self.name)  # Ensure we return a string

    class Meta:
        verbose_name = "Priority Level"
        verbose_name_plural = "Priority Levels"

class FavoriteType(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=7, default='#000000')  
    
    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Favorite Type"
        verbose_name_plural = "Favorite Types"

# Product categories with hierarchical support
class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    full_path = models.CharField(max_length=300, blank=True) 
    
    def save(self, *args, **kwargs):
        if self.parent and self.parent.full_path:
            self.full_path = f"{self.parent.full_path} / {self.name}"
        else:
            self.full_path = self.name
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.full_path)  

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"

# Company/Supplier model
class Company(models.Model):
    name = models.CharField(max_length=200)
    is_company = models.BooleanField(default=True)
    related_company = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    street = models.CharField(max_length=200, blank=True)
    zip_code = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return str(self.name)  

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

# Product types
class ProductType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return str(self.name)  

    class Meta:
        verbose_name = "Product Type"
        verbose_name_plural = "Product Types"

class PurchaseOrderStatusType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return str(self.name)  

    class Meta:
        verbose_name = "Purchase Order Status Type"
        verbose_name_plural = "Purchase Order Status Types"

# Main Product model
class Product(models.Model):
    favorite = models.ForeignKey(FavoriteType, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    internal_reference = models.CharField(max_length=100, null=True, blank=True)
    responsible = models.CharField(max_length=100, blank=True, null=True)
    barcode = models.CharField(max_length=100, blank=True, null=True)
    sales_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    cost = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    product_category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True)
    quantity_on_hand = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    forecasted_quantity = models.IntegerField(default=0)
    activity_exception_decoration = models.CharField(max_length=100, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.internal_reference:
            last_id = Product.objects.all().count() + 1
            self.internal_reference = f"PROD-{last_id:05d}"  
        super().save(*args, **kwargs)
    def __str__(self):
        return str(self.name)  

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

# Location model for inventory storage
class Location(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.code} - {self.name}" 

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"

# Purchase order model
class PurchaseOrder(models.Model):
    priority = models.ForeignKey(PriorityLevel, on_delete=models.SET_NULL, null=True)
    order_reference = models.CharField(max_length=100, unique=True)
    vendor = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='purchase_orders')
    purchase_representative = models.CharField(max_length=100, null=True, blank=True)
    order_deadline = models.DateTimeField()
    activities = models.TextField(blank=True)
    source_document = models.CharField(max_length=200, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    status = models.ForeignKey(PurchaseOrderStatusType, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return str(self.order_reference)  
    class Meta:
        verbose_name = "Purchase Order"
        verbose_name_plural = "Purchase Orders"

# Stock move types
class StockMoveType(models.Model):
    name = models.CharField(max_length=20, unique=True)
    code = models.CharField(max_length=10, unique=True)  
    def __str__(self):
        return str(self.name)  

    class Meta:
        verbose_name = "Stock Move Type"
        verbose_name_plural = "Stock Move Types"

# Stock move model for inventory movements
class StockMove(models.Model):
    move_type = models.ForeignKey(StockMoveType, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    from_location = models.ForeignKey(
        Location, on_delete=models.PROTECT, null=True, blank=True, related_name='outgoing_moves'
    )
    to_location = models.ForeignKey(
        Location, on_delete=models.PROTECT, null=True, blank=True, related_name='incoming_moves'
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def clean(self):
        """Validation rules based on move type"""
        if self.move_type.code == 'INBOUND' and self.from_location:
            raise ValidationError("INBOUND moves should not have a from_location")
        if self.move_type.code == 'OUTBOUND' and self.to_location:
            raise ValidationError("OUTBOUND moves should not have a to_location")
        if self.move_type.code == 'TRANSFER' and (not self.from_location or not self.to_location):
            raise ValidationError("TRANSFER moves require both from_location and to_location")

    def save(self, *args, **kwargs):
        self.full_clean()  
        super().save(*args, **kwargs)
        self.update_inventory()

    def update_inventory(self):
        """Update inventory levels for each move type"""
        try:
            if self.move_type.code == 'INBOUND':
                if not self.to_location:
                    raise ValueError("INBOUND moves require a to_location")

                inventory, created = InventoryLevel.objects.get_or_create(
                    product=self.product,
                    location=self.to_location,
                    defaults={'quantity': self.quantity}
                )
                if not created:
                    inventory.quantity += self.quantity
                    inventory.save()

            elif self.move_type.code == 'OUTBOUND':
                if not self.from_location:
                    raise ValueError("OUTBOUND moves require a from_location")

                inventory = InventoryLevel.objects.get(
                    product=self.product,
                    location=self.from_location
                )
                if inventory.quantity < self.quantity:
                    raise ValueError(f"Not enough stock for {self.product} in {self.from_location.code}")

                inventory.quantity -= self.quantity
                inventory.save()

            elif self.move_type.code == 'TRANSFER':
                if not self.from_location or not self.to_location:
                    raise ValueError("TRANSFER moves require both from_location and to_location")

                from_inventory = InventoryLevel.objects.get(
                    product=self.product,
                    location=self.from_location
                )
                if from_inventory.quantity < self.quantity:
                    raise ValueError(f"Not enough stock for {self.product} in {self.from_location.code}")

                from_inventory.quantity -= self.quantity
                from_inventory.save()

                to_inventory, created = InventoryLevel.objects.get_or_create(
                    product=self.product,
                    location=self.to_location,
                    defaults={'quantity': self.quantity}
                )
                if not created:
                    to_inventory.quantity += self.quantity
                    to_inventory.save()

        except InventoryLevel.DoesNotExist:
            raise ValueError(f"No inventory record found for {self.product} in source location.")

    def __str__(self):
        return f"{self.move_type} - {self.product} - {self.quantity}"

    class Meta:
        verbose_name = "Stock Move"
        verbose_name_plural = "Stock Moves"


# Inventory level per product and location
class InventoryLevel(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('product', 'location')
        verbose_name = "Inventory Level"
        verbose_name_plural = "Inventory Levels"
    
    def __str__(self):
        return f"{self.product} at {self.location} - {self.quantity}"  