from django.urls import path
from .views import RegisterAPI, LoginAPI, LogoutAPI, UserAPI, \
    InventoryItemListAPI, InventoryItemDetailAPI, \
    ExpenseListAPI, ExpenseDetailAPI, \
    IntangibleAssetListAPI, IntangibleAssetDetailAPI, \
    MachineryListAPI, MachineryDetailAPI, \
    HardwareSoftwareListAPI, HardwareSoftwareDetailAPI, \
    FurnitureListAPI, FurnitureDetailAPI, \
    InvestmentListAPI, InvestmentDetailAPI, \
    FixedAssetListAPI, FixedAssetDetailAPI, \
    ContractListAPI, ContractDetailAPI

urlpatterns = [
    # Authentication
    path('auth/register/', RegisterAPI.as_view(), name='register'),
    path('auth/login/', LoginAPI.as_view(), name='login'),
    path('auth/logout/', LogoutAPI.as_view(), name='logout'),

    # User API
    path('user/', UserAPI.as_view(), name='user'),

    # Inventory Management
    path('inventory/items/', InventoryItemListAPI.as_view(), name='inventory-item-list'),
    path('inventory/items/<int:pk>/', InventoryItemDetailAPI.as_view(), name='inventory-item-detail'),

    # Expense Management
    path('expenses/', ExpenseListAPI.as_view(), name='expense-list'),
    path('expenses/<int:pk>/', ExpenseDetailAPI.as_view(), name='expense-detail'),

    # Intangible Asset Management
    path('intangible-assets/', IntangibleAssetListAPI.as_view(), name='intangible-asset-list'),
    path('intangible-assets/<int:pk>/', IntangibleAssetDetailAPI.as_view(), name='intangible-asset-detail'),

    # Machinery and Vehicles Management
    path('machinery/', MachineryListAPI.as_view(), name='machinery-list'),
    path('machinery/<int:pk>/', MachineryDetailAPI.as_view(), name='machinery-detail'),

    # Hardware and Software Management
    path('hardware-software/', HardwareSoftwareListAPI.as_view(), name='hardware-software-list'),
    path('hardware-software/<int:pk>/', HardwareSoftwareDetailAPI.as_view(), name='hardware-software-detail'),

    # Furniture Management
    path('furniture/', FurnitureListAPI.as_view(), name='furniture-list'),
    path('furniture/<int:pk>/', FurnitureDetailAPI.as_view(), name='furniture-detail'),

    # Investments Management
    path('investments/', InvestmentListAPI.as_view(), name='investment-list'),
    path('investments/<int:pk>/', InvestmentDetailAPI.as_view(), name='investment-detail'),

    # Fixed Assets Management
    path('fixed-assets/', FixedAssetListAPI.as_view(), name='fixed-asset-list'),
    path('fixed-assets/<int:pk>/', FixedAssetDetailAPI.as_view(), name='fixed-asset-detail'),

    # Contract Management
    path('contracts/', ContractListAPI.as_view(), name='contract-list'),
    path('contracts/<int:pk>/', ContractDetailAPI.as_view(), name='contract-detail'),
]