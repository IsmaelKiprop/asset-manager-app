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
    ContractListAPI, ContractDetailAPI, \
    SavingsListAPI, SavingsDetailAPI, \
    BudgetListAPI, BudgetDetailAPI, \
    BankIntegrationListAPI, BankIntegrationDetailAPI, \
    BillListAPI, BillDetailAPI, \
    FinancialReportListAPI, FinancialReportDetailAPI

urlpatterns = [
    # Authentication
    path('auth/register/', RegisterAPI.as_view(), name='register'),
    path('auth/login/', LoginAPI.as_view(), name='login'),
    path('auth/logout/', LogoutAPI.as_view(), name='logout'),

    # User
    path('user/', UserAPI.as_view(), name='user'),

    # Inventory Management
    path('inventory/', InventoryItemListAPI.as_view(), name='inventory_list'),
    path('inventory/<int:pk>/', InventoryItemDetailAPI.as_view(), name='inventory_detail'),

    # Expense Management
    path('expenses/', ExpenseListAPI.as_view(), name='expense_list'),
    path('expenses/<int:pk>/', ExpenseDetailAPI.as_view(), name='expense_detail'),

    # Intangible Assets
    path('intangible-assets/', IntangibleAssetListAPI.as_view(), name='intangible_asset_list'),
    path('intangible-assets/<int:pk>/', IntangibleAssetDetailAPI.as_view(), name='intangible_asset_detail'),

    # Machinery and Vehicles
    path('machinery/', MachineryListAPI.as_view(), name='machinery_list'),
    path('machinery/<int:pk>/', MachineryDetailAPI.as_view(), name='machinery_detail'),

    # Hardware and Software
    path('hardware-software/', HardwareSoftwareListAPI.as_view(), name='hardware_software_list'),
    path('hardware-software/<int:pk>/', HardwareSoftwareDetailAPI.as_view(), name='hardware_software_detail'),

    # Furniture
    path('furniture/', FurnitureListAPI.as_view(), name='furniture_list'),
    path('furniture/<int:pk>/', FurnitureDetailAPI.as_view(), name='furniture_detail'),

    # Investments
    path('investments/', InvestmentListAPI.as_view(), name='investment_list'),
    path('investments/<int:pk>/', InvestmentDetailAPI.as_view(), name='investment_detail'),

    # Fixed Assets
    path('fixed-assets/', FixedAssetListAPI.as_view(), name='fixed_asset_list'),
    path('fixed-assets/<int:pk>/', FixedAssetDetailAPI.as_view(), name='fixed_asset_detail'),

    # Contracts
    path('contracts/', ContractListAPI.as_view(), name='contract_list'),
    path('contracts/<int:pk>/', ContractDetailAPI.as_view(), name='contract_detail'),

    # Financial Management
    path('savings/', SavingsListAPI.as_view(), name='savings_list'),
    path('savings/<int:pk>/', SavingsDetailAPI.as_view(), name='savings_detail'),

    path('budgets/', BudgetListAPI.as_view(), name='budget_list'),
    path('budgets/<int:pk>/', BudgetDetailAPI.as_view(), name='budget_detail'),

    path('bank-integrations/', BankIntegrationListAPI.as_view(), name='bank_integration_list'),
    path('bank-integrations/<int:pk>/', BankIntegrationDetailAPI.as_view(), name='bank_integration_detail'),

    path('bills/', BillListAPI.as_view(), name='bill_list'),
    path('bills/<int:pk>/', BillDetailAPI.as_view(), name='bill_detail'),

    path('financial-reports/', FinancialReportListAPI.as_view(), name='financial_report_list'),
    path('financial-reports/<int:pk>/', FinancialReportDetailAPI.as_view(), name='financial_report_detail'),
]