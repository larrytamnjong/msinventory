# pylint: disable=all

from django.db import migrations

def create_favorite_types(apps, schema_editor):
    FavoriteType = apps.get_model('msinventoryapp', 'FavoriteType')
    
    favorite_types = [
        {'name': 'Normal', 'description': 'Standard favorite type', 'color': '#007bff'},
        {'name': 'Important', 'description': 'High priority favorite', 'color': '#dc3545'},
        {'name': 'Special', 'description': 'Special treatment required', 'color': '#28a745'},
        {'name': 'Promotional', 'description': 'Promotional items', 'color': '#ffc107'},
    ]
    
    for fav_type in favorite_types:
        FavoriteType.objects.create(**fav_type)
        
def create_purchase_order_statuses(apps, schema_editor):
    FavoriteType = apps.get_model('msinventoryapp', 'PurchaseOrderStatusType')
    
    favorite_types = [
        {'name': 'Draft', 'description': 'Order is in draft state'},
        {'name': 'Confirmed', 'description': 'Order has been confirmed'},
        {'name': 'Done', 'description': 'Order is completed'},
        {'name': 'Cancelled', 'description': 'Order has been cancelled'},
    ]
    
    for fav_type in favorite_types:
        FavoriteType.objects.create(**fav_type)

def create_product_categories(apps, schema_editor):
    ProductCategory = apps.get_model('msinventoryapp', 'ProductCategory')
    
    # Create main categories first
    all_category = ProductCategory.objects.create(name='All', full_path='All')
    saleable = ProductCategory.objects.create(name='Saleable', parent=all_category, full_path='All / Saleable')
    
    # Create subcategories
    categories = [
        {'name': 'Office Furniture', 'parent': saleable},
        {'name': 'Electronics', 'parent': saleable},
        {'name': 'Stationery', 'parent': saleable},
        {'name': 'Consumables', 'parent': all_category},
        {'name': 'Raw Materials', 'parent': all_category},
    ]
    
    for category_data in categories:
        parent = category_data['parent']
        category = ProductCategory.objects.create(
            name=category_data['name'],
            parent=parent,
            full_path=f"{parent.full_path} / {category_data['name']}"
        )

def create_product_types(apps, schema_editor):
    ProductType = apps.get_model('msinventoryapp', 'ProductType')
    
    product_types = [
        {'name': 'Storable Product', 'description': 'Products that can be stored in inventory'},
        {'name': 'Consumable', 'description': 'Products that are consumed in operations'},
        {'name': 'Service', 'description': 'Non-tangible services'},
        {'name': 'Raw Material', 'description': 'Materials used in production'},
    ]
    
    for product_type in product_types:
        ProductType.objects.create(**product_type)

def create_priority_levels(apps, schema_editor):
    PriorityLevel = apps.get_model('msinventoryapp', 'PriorityLevel')
    
    priority_levels = [
        {'name': 'Low', 'description': 'Low priority items'},
        {'name': 'Medium', 'description': 'Medium priority items'},
        {'name': 'High', 'description': 'High priority items'},
        {'name': 'Urgent', 'description': 'Urgent priority items'},
    ]
    
    for priority in priority_levels:
        PriorityLevel.objects.create(**priority)

def create_stock_move_types(apps, schema_editor):
    StockMoveType = apps.get_model('msinventoryapp', 'StockMoveType')
    
    move_types = [
        {'name': 'Inbound', 'code': 'INBOUND'},
        {'name': 'Outbound', 'code': 'OUTBOUND'},
        {'name': 'Transfer', 'code': 'TRANSFER'},
    ]
    
    for move_type in move_types:
        StockMoveType.objects.create(**move_type)

def create_locations(apps, schema_editor):
    Location = apps.get_model('msinventoryapp', 'Location')
    
    locations = [
        {'code': 'WH-MAIN', 'name': 'Main Warehouse', 'description': 'Primary storage location'},
        {'code': 'WH-SEC', 'name': 'Secondary Warehouse', 'description': 'Backup storage location'},
        {'code': 'STORE-1', 'name': 'Retail Store 1', 'description': 'Main retail outlet'},
        {'code': 'STORE-2', 'name': 'Retail Store 2', 'description': 'Secondary retail outlet'},
        {'code': 'PROD-LINE', 'name': 'Production Line', 'description': 'Manufacturing area'},
    ]
    
    for location in locations:
        Location.objects.create(**location)

def create_companies(apps, schema_editor):
    Company = apps.get_model('msinventoryapp', 'Company')
    
    companies = [
        {
            'name': 'Office Supplies Ltd',
            'is_company': True,
            'street': '123 Business Ave',
            'zip_code': '10001',
            'city': 'New York',
            'state': 'NY',
            'country': 'USA'
        },
        {
            'name': 'Tech Gadgets Inc',
            'is_company': True,
            'street': '456 Tech Street',
            'zip_code': '90001',
            'city': 'Los Angeles',
            'state': 'CA',
            'country': 'USA'
        },
        {
            'name': 'Furniture World',
            'is_company': True,
            'street': '789 Design Blvd',
            'zip_code': '60601',
            'city': 'Chicago',
            'state': 'IL',
            'country': 'USA'
        },
    ]
    
    for company in companies:
        Company.objects.create(**company)

class Migration(migrations.Migration):

    dependencies = [
        ('msinventoryapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_purchase_order_statuses),
        migrations.RunPython(create_favorite_types),
        migrations.RunPython(create_product_categories),
        migrations.RunPython(create_product_types),
        migrations.RunPython(create_priority_levels),
        migrations.RunPython(create_stock_move_types),
        migrations.RunPython(create_locations),
        migrations.RunPython(create_companies),
    ]