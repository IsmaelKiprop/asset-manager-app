from django.urls import path
from .views import RegisterAPI, LoginAPI, LogoutAPI, UserAPI, InventoryItemListAPI, InventoryItemDetailAPI, \
    ExpenseListAPI, ExpenseDetailAPI, IntangibleAssetListAPI, IntangibleAssetDetailAPI, MachineryListAPI, \
    MachineryDetailAPI, HardwareSoftwareListAPI, HardwareSoftwareDetailAPI, FurnitureListAPI, FurnitureDetailAPI, \
    InvestmentListAPI, InvestmentDetailAPI, FixedAssetListAPI, FixedAssetDetailAPI, ContractListAPI, \
    ContractDetailAPI, SavingsListAPI, SavingsDetailAPI, BudgetListAPI, BudgetDetailAPI, BankIntegrationListAPI, \
    BankIntegrationDetailAPI, BillListAPI, BillDetailAPI, FinancialReportListAPI, FinancialReportDetailAPI

urlpatterns = [
    path('api/auth/register/', RegisterAPI.as_view()),
    path('api/auth/login/', LoginAPI.as_view()),
    path('api/auth/logout/', LogoutAPI.as_view()),
    path('api/auth/user/', UserAPI.as_view()),

    # Inventory Management URLs
    path('api/inventory/', InventoryItemListAPI.as_view()),
    path('api/inventory/<int:pk>/', InventoryItemDetailAPI.as_view()),

    # Expense Management URLs
    path('api/expense/', ExpenseListAPI.as_view()),
    path('api/expense/<int:pk>/', ExpenseDetailAPI.as_view()),

    # Intangible Assets URLs
    path('api/intangible-assets/', IntangibleAssetListAPI.as_view()),
    path('api/intangible-assets/<int:pk>/', IntangibleAssetDetailAPI.as_view()),

    # Machinery and Vehicles URLs
    path('api/machinery/', MachineryListAPI.as_view()),
    path('api/machinery/<int:pk>/', MachineryDetailAPI.as_view()),

    # Hardware and Software URLs
    path('api/hardware-software/', HardwareSoftwareListAPI.as_view()),
    path('api/hardware-software/<int:pk>/', HardwareSoftwareDetailAPI.as_view()),

    # Furniture URLs
    path('api/furniture/', FurnitureListAPI.as_view()),
    path('api/furniture/<int:pk>/', FurnitureDetailAPI.as_view()),

    # Investment URLs
    path('api/investment/', InvestmentListAPI.as_view()),
    path('api/investment/<int:pk>/', InvestmentDetailAPI.as_view()),

    # Fixed Assets URLs
    path('api/fixed-asset/', FixedAssetListAPI.as_view()),
    path('api/fixed-asset/<int:pk>/', FixedAssetDetailAPI.as_view()),

    # Contract Management URLs
    path('api/contract/', ContractListAPI.as_view()),
    path('api/contract/<int:pk>/', ContractDetailAPI.as_view()),

    # Financial Management URLs
    path('api/savings/', SavingsListAPI.as_view()),
    path('api/savings/<int:pk>/', SavingsDetailAPI.as_view()),
    path('api/budget/', BudgetListAPI.as_view()),
    path('api/budget/<int:pk>/', BudgetDetailAPI.as_view()),
    path('api/bank-integration/', BankIntegrationListAPI.as_view()),
    path('api/bank-integration/<int:pk>/', BankIntegrationDetailAPI.as_view()),
    path('api/bill/', BillListAPI.as_view()),
    path('api/bill/<int:pk>/', BillDetailAPI.as_view()),
    path('api/financial-report/', FinancialReportListAPI.as_view()),
    path('api/financial-report/<int:pk>/', FinancialReportDetailAPI.as_view()),
]