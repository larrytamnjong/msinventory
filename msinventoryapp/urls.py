

from django.urls import path, include
from .views import (
    PriorityLevelViewSet, FavoriteTypeViewSet, ProductCategoryViewSet,
    CompanyViewSet, ProductTypeViewSet, PurchaseOrderStatusTypeViewSet,
    LocationViewSet, ProductViewSet, PurchaseOrderViewSet,
    StockMoveTypeViewSet, StockMoveViewSet, InventoryLevelViewSet
)
from rest_framework.routers import DefaultRouter
# pylint: disable=all

router = DefaultRouter()
router.register(r'priority-levels', PriorityLevelViewSet)
router.register(r'favorite-types', FavoriteTypeViewSet)
router.register(r'product-categories', ProductCategoryViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'product-types', ProductTypeViewSet)
router.register(r'purchase-order-status-types', PurchaseOrderStatusTypeViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'products', ProductViewSet)
router.register(r'purchase-orders', PurchaseOrderViewSet)
router.register(r'stock-move-types', StockMoveTypeViewSet)
router.register(r'stock-moves', StockMoveViewSet)
router.register(r'inventory-levels', InventoryLevelViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]