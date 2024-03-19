from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
import binascii
import os

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    company_name = models.CharField(_('company name'), max_length=100)
    location = models.CharField(_('location'), max_length=100)
    number_of_employees = models.PositiveIntegerField(_('number of employees'), default=0)
    industry = models.CharField(_('industry'), max_length=100)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['company_name', 'location', 'number_of_employees', 'industry']

    def __str__(self):
        return self.email

# Choices for industries
INDUSTRY_CHOICES = [
    ('Aerospace', 'Aerospace'),
    ('Agriculture', 'Agriculture'),
    ('Automotive', 'Automotive'),
    ('Basic Metal Production', 'Basic Metal Production'),
    ('Chemical', 'Chemical'),
    ('Clothing', 'Clothing'),
    ('Commerce', 'Commerce'),
    ('Construction', 'Construction'),
    ('Culture', 'Culture'),
    ('Education', 'Education'),
    ('Electricity', 'Electricity'),
    ('Electronics', 'Electronics'),
    ('Finance', 'Finance'),
    ('Food and Drink', 'Food and Drink'),
    ('Forestry', 'Forestry'),
    ('Health', 'Health'),
    ('Logistics', 'Logistics'),
    ('Tourism', 'Tourism'),
    ('Marine', 'Marine'),
    ('Mining', 'Mining'),
    ('Media', 'Media'),
    ('Oil and Gas', 'Oil and Gas'),
    ('Postal and Telecommunications', 'Postal and Telecommunications'),
    ('Retail Stores', 'Retail Stores'),
    ('Textiles', 'Textiles'),
    ('Railways', 'Railways'),
    ('Road Transport', 'Road Transport'),
    ('Wholesale Stores', 'Wholesale Stores'),
    ('Other', 'Other'),
]

# Choices for demand categories
DEMAND_CATEGORIES_CHOICES = [
    ('Highest demand', 'Highest demand (90%-100%)'),
    ('High Demand', 'High Demand (70%-89%)'),
    ('Medium Demand', 'Medium Demand (50%-69%)'),
    ('Low Demand', 'Low Demand (40%-49%)'),
    ('Very Low', 'Very Low (39% and Below)'),
]

# Choices for value categories
VALUE_CATEGORIES_CHOICES = [
    ('Highest value', 'Highest value'),
    ('High Value', 'High Value'),
    ('Medium Value', 'Medium Value'),
    ('Low Value', 'Low Value'),
    ('Very Low Value', 'Very Low Value'),
]

class InventoryItem(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)  # Multicurrency support
    photo = models.ImageField(upload_to='inventory_photos/')
    industry = models.CharField(max_length=100, choices=INDUSTRY_CHOICES)
    demand_category = models.CharField(max_length=100, choices=DEMAND_CATEGORIES_CHOICES, default='Medium Demand')
    value_category = models.CharField(max_length=100, choices=VALUE_CATEGORIES_CHOICES, default='Medium Value')
    stock_notification_threshold = models.PositiveIntegerField(default=0)
    barcode = models.CharField(max_length=100, blank=True, null=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    rfid_tag = models.CharField(max_length=100, blank=True, null=True)
    iot_identifier = models.CharField(max_length=100, blank=True, null=True)
    warehouse = models.CharField(max_length=100, blank=True, null=True)
    place_of_sale = models.CharField(max_length=100, blank=True, null=True)
    is_returnable = models.BooleanField(default=False)
    proceed_to_pay = models.BooleanField(default=True)
    is_self_service = models.BooleanField(default=True)
    automated_purchasing = models.BooleanField(default=False)
    just_in_time_management = models.BooleanField(default=False)
    real_time_stock_tracking = models.BooleanField(default=True)
    lost_stolen_damaged = models.BooleanField(default=True)
    demand_record = models.PositiveIntegerField(default=0)
    people_requested = models.PositiveIntegerField(default=0)
    invoices = models.FileField(upload_to='invoices/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    taxes = models.DecimalField(max_digits=10, decimal_places=2)
    cost_per_item = models.DecimalField(max_digits=10, decimal_places=2)
    stock_value = models.DecimalField(max_digits=10, decimal_places=2)

    def get_sales_history(self):
        # Logic to retrieve sales history for this item
        pass

# Expense model
class Expense(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField()
    category = models.CharField(max_length=100, choices=DEMAND_CATEGORIES_CHOICES)

# Invoice model
class Invoice(models.Model):
    invoice_number = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()

# Bank connection model
class BankConnection(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    routing_number = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

# VAT model
class VAT(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    vat_number = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=5, decimal_places=2)

# Report model
class Report(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    report_type = models.CharField(max_length=100)
    content = models.TextField()

# Employee model
class Employee(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=100)

# Currency model
class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=50)

# Transaction model
class Transaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField()
    recurring = models.BooleanField(default=False)

# Inventory model
class Inventory(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

# Project model
class Project(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2)

# Warehouse model
class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    manager = models.ForeignKey('CustomUser', on_delete=models.CASCADE)  # Assuming CustomUser model exists

# Stock return model
class StockReturn(models.Model):
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    return_reason = models.TextField()
    return_date = models.DateField()

# Stock request model
class StockRequest(models.Model):
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    requested_quantity = models.PositiveIntegerField()
    request_date = models.DateField()
    requester = models.ForeignKey('CustomUser', on_delete=models.CASCADE)  # Assuming CustomUser model exists


# Models for Finance Management

# Savings model
class Savings(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    target_date = models.DateField()
    current_balance = models.DecimalField(max_digits=10, decimal_places=2)

# Budget model
class Budget(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    budget_amount = models.DecimalField(max_digits=10, decimal_places=2)
    actual_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

# Bank integration model
class BankIntegration(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

# Bill manager model
class Bill(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()

# Analytics model
class Analytics(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cash_flow = models.DecimalField(max_digits=10, decimal_places=2)
    budgeting = models.DecimalField(max_digits=10, decimal_places=2)
    net_worth = models.DecimalField(max_digits=10, decimal_places=2)
    transactions = models.DecimalField(max_digits=10, decimal_places=2)

# Assets valuation model
class AssetsValuation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    asset_name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

# Credit score tracking model
class CreditScore(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    date = models.DateField()

# Customizable alerts model
class CustomizableAlert(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    alert_type = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateField()

# Financial growth tracking model
class FinancialGrowth(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    growth_type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

# Checking account model
class CheckingAccount(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=100)
    digital_check = models.BooleanField(default=True)

# Insurance model
class Insurance(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    premium_amount = models.DecimalField(max_digits=10, decimal_places=2)
    coverage_amount = models.DecimalField(max_digits=10, decimal_places=2)

# Investing model
class Investing(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    target_date = models.DateField()
    current_balance = models.DecimalField(max_digits=10, decimal_places=2)

# Integration with accounting software model
class AccountingSoftwareIntegration(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    software_name = models.CharField(max_length=100)
    integration_type = models.CharField(max_length=100)

# Intangible Asset model
# Models for Intangible Assets Management

# Intangible Asset Industry model
class IntangibleAssetIndustry(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Intangible Asset Category model
class IntangibleAssetCategory(models.Model):
    name = models.CharField(max_length=100)
    industry = models.ForeignKey(IntangibleAssetIndustry, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Intangible Asset model
class IntangibleAsset(models.Model):
    category = models.ForeignKey(IntangibleAssetCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_registered = models.DateField()
    expiring_date = models.DateField(null=True, blank=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_created', 'name']

# Asset Document model
class AssetDocument(models.Model):
    asset = models.ForeignKey(IntangibleAsset, on_delete=models.CASCADE)
    document = models.FileField(upload_to='asset_documents/')
    description = models.TextField()

# Model for people concerned
class ConcernedPeople(models.Model):
    asset = models.ForeignKey(IntangibleAsset, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=100)

# Sorting options
SORT_OPTIONS = [
    ('category', 'Category'),
    ('date_created_asc', 'Date Created (Ascending)'),
    ('date_created_desc', 'Date Created (Descending)'),
    ('date_modified_asc', 'Date Modified (Ascending)'),
    ('date_modified_desc', 'Date Modified (Descending)'),
    ('expiring_date_asc', 'Expiring Date (Ascending)'),
    ('expiring_date_desc', 'Expiring Date (Descending)'),
]

# Notification for expiring assets
class ExpiringAsset(models.Model):
    asset = models.ForeignKey(IntangibleAsset, on_delete=models.CASCADE)
    notification_date = models.DateField()
    notified = models.BooleanField(default=False)

# Total Value of all assets (computed property)
class TotalAssetValue(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    total_value = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def calculate_total_value(self):
        total = IntangibleAsset.objects.filter(owner=self.user).aggregate(Sum('value'))['value__sum']
        self.total_value = total if total else 0
        self.save()

# Add, Edit, and Delete functionalities are handled through Django admin panel


# Models for Computer Software

#User = CustomUserManager.create_user()

# Choices for industries including "Other" option
INDUSTRY_CHOICES = [
    ('Aerospace', 'Aerospace'),
    ('Agriculture', 'Agriculture'),
    ('Automotive', 'Automotive'),
    ('Other', 'Other'),
]

# Choices for software categories
# Customize categories of software
SOFTWARE_CATEGORY_CHOICES = [
    ('Category1', 'Category 1'),
    ('Category2', 'Category 2'),
    # Add more categories as needed
]

class ComputerSoftware(models.Model):
    industry = models.CharField(max_length=100, choices=INDUSTRY_CHOICES)
    category = models.CharField(max_length=100, choices=SOFTWARE_CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    date_registered = models.DateField()
    expiring_date = models.DateField(blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    documentation = models.FileField(upload_to='software_documents/')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE) #changes
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class SoftwareDocument(models.Model):
    software = models.ForeignKey(ComputerSoftware, on_delete=models.CASCADE)
    document = models.FileField(upload_to='software_documents/')
    description = models.TextField()

class ConcernedPeople(models.Model):
    software = models.ForeignKey(ComputerSoftware, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=100)

# Sorting options with verbose names
SORT_OPTIONS = {
    'category': _('Category'),
    'date_created_asc': _('Date Created (Ascending)'),
    'date_created_desc': _('Date Created (Descending)'),
    'date_modified_asc': _('Date Modified (Ascending)'),
    'date_modified_desc': _('Date Modified (Descending)'),
    'expiring_date_asc': _('Expiring Date (Ascending)'),
    'expiring_date_desc': _('Expiring Date (Descending)'),
}

# Models for Computer Hardware

#User = get_user_model()

# Choices for industries including "Other" option
INDUSTRY_CHOICES = [
    ('Aerospace', 'Aerospace'),
    ('Agriculture', 'Agriculture'),
    ('Automotive', 'Automotive'),
    ('Other', 'Other'),
]

# Choices for hardware categories
# Customize categories of hardware
HARDWARE_CATEGORY_CHOICES = [
    ('Category1', 'Category 1'),
    ('Category2', 'Category 2'),
    # Add more categories as needed
]

# Choices for hardware value categories
VALUE_CATEGORIES_CHOICES = [
    ('Highest value', 'Highest value'),
    ('High Value', 'High Value'),
    ('Medium Value', 'Medium Value'),
    ('Low Value', 'Low Value'),
    ('Very Low Value', 'Very Low Value'),
]

class ComputerHardware(models.Model):
    industry = models.CharField(max_length=100, choices=INDUSTRY_CHOICES)
    name = models.CharField(max_length=100)
    date_registered = models.DateField()
    date_manufactured = models.DateField()
    expiry_date_warranty = models.DateField()
    warranty_length = models.PositiveIntegerField(help_text="Length of warranty in years")
    location = models.CharField(max_length=100)
    malfunction = models.BooleanField(default=False)
    malfunction_details = models.TextField(blank=True, null=True)
    malfunction_date = models.DateField(blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    documentation = models.FileField(upload_to='hardware_documents/')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE) #changes
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class HardwareDocument(models.Model):
    hardware = models.ForeignKey(ComputerHardware, on_delete=models.CASCADE)
    document = models.FileField(upload_to='hardware_documents/')
    description = models.TextField()

class ConcernedPeople(models.Model):
    hardware = models.ForeignKey(ComputerHardware, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=100)

class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE) #changes

# Sorting options with verbose names
SORT_OPTIONS = {
    'category': _('Category'),
    'date_created_asc': _('Date Created (Ascending)'),
    'date_created_desc': _('Date Created (Descending)'),
    'date_modified_asc': _('Date Modified (Ascending)'),
    'date_modified_desc': _('Date Modified (Descending)'),
    'expiry_date_warranty_asc': _('Expiry Date of Warranty (Ascending)'),
    'expiry_date_warranty_desc': _('Expiry Date of Warranty (Descending)'),
    'service_date_asc': _('Service Date (Ascending)'),
    'service_date_desc': _('Service Date (Descending)'),
    'repair_dates_asc': _('Repair Dates (Ascending)'),
    'repair_dates_desc': _('Repair Dates (Descending)'),
    'date_manufactured_asc': _('Date of Manufacture (Ascending)'),
    'date_manufactured_desc': _('Date of Manufacture (Descending)'),
}

# Machinery Model

#User = get_user_model()

# Choices for industries including "Other" option
INDUSTRY_CHOICES = [
    ('Aerospace', 'Aerospace'),
    ('Agriculture', 'Agriculture'),
    ('Automotive', 'Automotive'),
    ('Other', 'Other'),
]

# Choices for machine categories
# Customize categories of machines
MACHINE_CATEGORY_CHOICES = [
    ('Category1', 'Category 1'),
    ('Category2', 'Category 2'),
    # Add more categories as needed
]

# Choices for machine value categories
VALUE_CATEGORIES_CHOICES = [
    ('Highest value', 'Highest value'),
    ('High Value', 'High Value'),
    ('Medium Value', 'Medium Value'),
    ('Low Value', 'Low Value'),
    ('Very Low Value', 'Very Low Value'),
]

class Machinery(models.Model):
    industry = models.CharField(max_length=100, choices=INDUSTRY_CHOICES)
    name = models.CharField(max_length=100)
    date_registered = models.DateField()
    date_manufactured = models.DateField()
    expiry_date_warranty = models.DateField()
    warranty_length = models.PositiveIntegerField(help_text="Length of warranty in years")
    location = models.CharField(max_length=100)
    malfunction = models.BooleanField(default=False)
    malfunction_details = models.TextField(blank=True, null=True)
    malfunction_date = models.DateField(blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    documentation = models.FileField(upload_to='machinery_documents/')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE) #changes
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class MachineryDocument(models.Model):
    machinery = models.ForeignKey(Machinery, on_delete=models.CASCADE)
    document = models.FileField(upload_to='machinery_documents/')
    description = models.TextField()

class ConcernedPeople(models.Model):
    machinery = models.ForeignKey(Machinery, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=100)

class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE) #changes

class WarrantyRecord(models.Model):
    machinery = models.ForeignKey(Machinery, on_delete=models.CASCADE)
    warranty_used = models.BooleanField(default=False)
    broken_details = models.TextField(blank=True, null=True)
    broken_date = models.DateField(blank=True, null=True)
    service_date = models.DateField(blank=True, null=True)
    repair_details = models.TextField(blank=True, null=True)
    repair_date = models.DateField(blank=True, null=True)

class PurchaseRecord(models.Model):
    machinery = models.ForeignKey(Machinery, on_delete=models.CASCADE)
    receipt = models.FileField(upload_to='purchase_records/')
    other_documentation = models.FileField(upload_to='purchase_records/', blank=True, null=True)

class RepairRecord(models.Model):
    machinery = models.ForeignKey(Machinery, on_delete=models.CASCADE)
    repair_details = models.TextField()
    repair_date = models.DateField()

# Sorting options with verbose names
SORT_OPTIONS = {
    'category': _('Category'),
    'date_created_asc': _('Date Created (Ascending)'),
    'date_created_desc': _('Date Created (Descending)'),
    'date_modified_asc': _('Date Modified (Ascending)'),
    'date_modified_desc': _('Date Modified (Descending)'),
    'expiry_date_warranty_asc': _('Expiry Date of Warranty (Ascending)'),
    'expiry_date_warranty_desc': _('Expiry Date of Warranty (Descending)'),
    'service_date_asc': _('Service Date (Ascending)'),
    'service_date_desc': _('Service Date (Descending)'),
    'repair_dates_asc': _('Repair Dates (Ascending)'),
    'repair_dates_desc': _('Repair Dates (Descending)'),
    'date_manufactured_asc': _('Date of Manufacture (Ascending)'),
    'date_manufactured_desc': _('Date of Manufacture (Descending)'),
}

#Investment Model 

#User = get_user_model()

# Choices for industries including "Other" option
INDUSTRY_CHOICES = [
    ('Aerospace', 'Aerospace'),
    ('Agriculture', 'Agriculture'),
    ('Automotive', 'Automotive'),
    ('Other', 'Other'),
]

# Choices for investment categories
# Customize categories of investments
INVESTMENT_CATEGORY_CHOICES = [
    ('Stocks', 'Stocks'),
    ('Bonds', 'Bonds'),
    ('Mutual Funds and ETFs', 'Mutual Funds and ETFs'),
    ('Bank Products', 'Bank Products'),
    ('Options', 'Options'),
    ('Annuities', 'Annuities'),
    ('Retirement Benefits', 'Retirement Benefits'),
    ('Alternative and Complex Products', 'Alternative and Complex Products'),
    ('Savings for Education', 'Savings for Education'),
    ('Initial Coin Offerings and Cryptocurrencies', 'Initial Coin Offerings and Cryptocurrencies'),
    ('Commodity Features', 'Commodity Features'),
    ('Security Features', 'Security Features'),
    ('Insurance', 'Insurance'),
    # Add more categories as needed
]

# Choices for investment value categories
VALUE_CATEGORIES_CHOICES = [
    ('Highest value', 'Highest value'),
    ('High Value', 'High Value'),
    ('Medium Value', 'Medium Value'),
    ('Low Value', 'Low Value'),
    ('Very Low Value', 'Very Low Value'),
]

class Investment(models.Model):
    industry = models.CharField(max_length=100, choices=INDUSTRY_CHOICES)
    name = models.CharField(max_length=100)
    date_registered = models.DateField()
    date_manufactured = models.DateField()
    expiry_date = models.DateField()
    location = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    documentation = models.FileField(upload_to='investment_documents/')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE) #changes
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class InvestmentDocument(models.Model):
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE)
    document = models.FileField(upload_to='investment_documents/')
    description = models.TextField()

class ConcernedPeople(models.Model):
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=100)

# Sorting options with verbose names
SORT_OPTIONS = {
    'category': _('Category'),
    'date_created_asc': _('Date Created (Ascending)'),
    'date_created_desc': _('Date Created (Descending)'),
    'date_modified_asc': _('Date Modified (Ascending)'),
    'date_modified_desc': _('Date Modified (Descending)'),
}

#Furniture Model

#User = get_user_model()

# Choices for industries including "Other" option
INDUSTRY_CHOICES = [
    ('Aerospace', 'Aerospace'),
    ('Agriculture', 'Agriculture'),
    ('Automotive', 'Automotive'),
    ('Other', 'Other'),
]

# Choices for furniture categories
# Customize categories of furniture
FURNITURE_CATEGORY_CHOICES = [
    ('Category1', 'Category 1'),
    ('Category2', 'Category 2'),
    # Add more categories as needed
]

# Choices for furniture value categories
VALUE_CATEGORIES_CHOICES = [
    ('Highest value', 'Highest value'),
    ('High Value', 'High Value'),
    ('Medium Value', 'Medium Value'),
    ('Low Value', 'Low Value'),
    ('Very Low Value', 'Very Low Value'),
]

class Furniture(models.Model):
    industry = models.CharField(max_length=100, choices=INDUSTRY_CHOICES)
    name = models.CharField(max_length=100)
    date_registered = models.DateField()
    date_manufactured = models.DateField()
    expiry_date_warranty = models.DateField()
    warranty_length = models.PositiveIntegerField(help_text="Length of warranty in years")
    location = models.CharField(max_length=100)
    malfunction = models.BooleanField(default=False)
    malfunction_details = models.TextField(blank=True, null=True)
    malfunction_date = models.DateField(blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    documentation = models.FileField(upload_to='furniture_documents/')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE) #changes
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class FurnitureDocument(models.Model):
    furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE)
    document = models.FileField(upload_to='furniture_documents/')
    description = models.TextField()

class ConcernedPeople(models.Model):
    furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=100)

class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE) #changes

class WarrantyRecord(models.Model):
    furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE)
    warranty_used = models.BooleanField(default=False)
    broken_details = models.TextField(blank=True, null=True)
    broken_date = models.DateField(blank=True, null=True)
    service_date = models.DateField(blank=True, null=True)
    repair_details = models.TextField(blank=True, null=True)
    repair_date = models.DateField(blank=True, null=True)
    date_of_manufacture = models.DateField()

class PurchaseRecord(models.Model):
    furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE)
    receipt = models.FileField(upload_to='purchase_records/')
    other_documentation = models.FileField(upload_to='purchase_records/')

# Other models such as repair records, etc. can be added similarly

# Sorting options with verbose names
SORT_OPTIONS = {
    'category': _('Category'),
    'date_created_asc': _('Date Created (Ascending)'),
    'date_created_desc': _('Date Created (Descending)'),
    'date_modified_asc': _('Date Modified (Ascending)'),
    'date_modified_desc': _('Date Modified (Descending)'),
    'expiry_date_warranty_asc': _('Expiry Date of Warranty (Ascending)'),
    'expiry_date_warranty_desc': _('Expiry Date of Warranty (Descending)'),
    'service_date_asc': _('Service Date (Ascending)'),
    'service_date_desc': _('Service Date (Descending)'),
    'repair_dates_asc': _('Repair Dates (Ascending)'),
    'repair_dates_desc': _('Repair Dates (Descending)'),
    'date_manufactured_asc': _('Date of Manufacture (Ascending)'),
    'date_manufactured_desc': _('Date of Manufacture (Descending)'),
}

# Choices for investment categories
# Customize categories of investments
INVESTMENT_CATEGORY_CHOICES = [
    ('Stocks', 'Stocks'),
    ('Bonds', 'Bonds'),
    ('Mutual Funds and ETFs', 'Mutual Funds and ETFs'),
    ('Bank Products', 'Bank Products'),
    ('Options', 'Options'),
    ('Annuities', 'Annuities'),
    ('Retirement Benefits', 'Retirement Benefits'),
    ('Alternative and Complex Products', 'Alternative and Complex Products'),
    ('Savings for Education', 'Savings for Education'),
    ('Initial Coin Offerings and Cryptocurrencies', 'Initial Coin Offerings and Cryptocurrencies'),
    ('Commodity Features', 'Commodity Features'),
    ('Security Features', 'Security Features'),
    ('Insurance', 'Insurance'),
    # Add more categories as needed
]

class Investment(models.Model):
    industry = models.CharField(max_length=100, choices=INDUSTRY_CHOICES)
    category = models.CharField(max_length=100, choices=INVESTMENT_CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    date_registered = models.DateField()
    date_manufactured = models.DateField()
    expiry_date = models.DateField()
    location = models.CharField(max_length=100)
    malfunction = models.BooleanField(default=False)
    malfunction_details = models.TextField(blank=True, null=True)
    malfunction_date = models.DateField(blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    documentation = models.FileField(upload_to='investment_documents/')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE) #changes
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Furniture model continued
class FurnitureQRCode(models.Model):
    furniture = models.OneToOneField(Furniture, on_delete=models.CASCADE)
    qr_code_image = models.ImageField(upload_to='furniture_qr_codes/')

# Investments model continued
class InvestmentDocument(models.Model):
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE)
    document = models.FileField(upload_to='investment_documents/')
    description = models.TextField()

class InvestmentConcernedPeople(models.Model):
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=100)

class InvestmentPurchaseRecord(models.Model):
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE)
    receipt = models.FileField(upload_to='investment_purchase_records/')
    other_documentation = models.FileField(upload_to='investment_purchase_records/')

class WarrantyRecord(models.Model):
    #asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    warranty_provider = models.CharField(max_length=100)
    warranty_details = models.TextField()

class RepairRecord(models.Model):
    #asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    repair_date = models.DateField()
    repair_details = models.TextField()

class ServiceRecord(models.Model):
    #asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    service_date = models.DateField()
    service_details = models.TextField()

class PurchaseRecord(models.Model):
    #asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    purchase_date = models.DateField()
    purchase_details = models.TextField()

class BarcodeScanner(models.Model):
    #asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    barcode_image = models.ImageField(upload_to='barcode_scanner_images/')

class QRCodeScanner(models.Model):
    #asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    qr_code_image = models.ImageField(upload_to='qr_code_scanner_images/')

class RFIDTag(models.Model):
    #asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    tag_code = models.CharField(max_length=100)

class IOTDevice(models.Model):
    #asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    device_id = models.CharField(max_length=100)

class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE) #changes

#Fixed Assets Model

class FixedAsset(models.Model):
    industry = models.CharField(max_length=100, choices=INDUSTRY_CHOICES)
    name = models.CharField(max_length=100)
    date_registered = models.DateField()
    date_manufactured = models.DateField()
    expiry_date_warranty = models.DateField()
    warranty_length = models.PositiveIntegerField(help_text="Length of warranty in years")
    location = models.CharField(max_length=100)
    malfunction = models.BooleanField(default=False)
    malfunction_details = models.TextField(blank=True, null=True)
    malfunction_date = models.DateField(blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    documentation = models.FileField(upload_to='fixed_assets_documents/')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class FixedAssetDocument(models.Model):
    fixed_asset = models.ForeignKey(FixedAsset, on_delete=models.CASCADE)
    document = models.FileField(upload_to='fixed_assets_documents/')
    description = models.TextField()

class FixedAssetConcernedPeople(models.Model):
    fixed_asset = models.ForeignKey(FixedAsset, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=100)

class LeaseRecord(models.Model):
    fixed_asset = models.ForeignKey(FixedAsset, on_delete=models.CASCADE)
    lease_expiry_date = models.DateField()

class BarcodeScanner(models.Model):
    asset = models.ForeignKey(FixedAsset, on_delete=models.CASCADE)
    barcode_image = models.ImageField(upload_to='barcode_scanner_images/')

class QRCodeScanner(models.Model):
    asset = models.ForeignKey(FixedAsset, on_delete=models.CASCADE)
    qr_code_image = models.ImageField(upload_to='qr_code_scanner_images/')

class RFIDTag(models.Model):
    asset = models.ForeignKey(FixedAsset, on_delete=models.CASCADE)
    tag_code = models.CharField(max_length=100)

class IOTDevice(models.Model):
    asset = models.ForeignKey(FixedAsset, on_delete=models.CASCADE)
    device_id = models.CharField(max_length=100)

class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE) #changes

#Contract Management Model

#User = get_user_model()

# Choices for industries including "Other" option
INDUSTRY_CHOICES = [
    ('Aerospace', 'Aerospace'),
    ('Agriculture', 'Agriculture'),
    ('Automotive', 'Automotive'),
    ('Other', 'Other'),
]

# Choices for contract categories
# Customize categories of contracts
CONTRACT_CATEGORY_CHOICES = [
    ('Category1', 'Category 1'),
    ('Category2', 'Category 2'),
    # Add more categories as needed
]

class Contract(models.Model):
    industry = models.CharField(max_length=100, choices=INDUSTRY_CHOICES)
    category = models.CharField(max_length=100, choices=CONTRACT_CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    date_acquired = models.DateField()
    expiry_date = models.DateField(blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    documentation = models.FileField(upload_to='contract_documents/')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE) #changes
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ContractDocument(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    document = models.FileField(upload_to='contract_documents/')
    description = models.TextField()

class ConcernedPeople(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=100)

# Sorting options with verbose names
SORT_OPTIONS = {
    'category': _('Category'),
    'date_created_asc': _('Date Created (Ascending)'),
    'date_created_desc': _('Date Created (Descending)'),
    'date_modified_asc': _('Date Modified (Ascending)'),
    'date_modified_desc': _('Date Modified (Descending)'),
    'expiry_date_asc': _('Expiry Date (Ascending)'),
    'expiry_date_desc': _('Expiry Date (Descending)'),
}

#Vehicle Model 

#User = get_user_model()

# Choices for industries including "Other" option
INDUSTRY_CHOICES = [
    ('Aerospace', 'Aerospace'),
    ('Agriculture', 'Agriculture'),
    ('Automotive', 'Automotive'),
    ('Other', 'Other'),
]

# Choices for vehicle categories
# Customize categories of vehicles
VEHICLE_CATEGORY_CHOICES = [
    ('Sedan', 'Sedan'),
    ('SUV', 'SUV'),
    ('Truck', 'Truck'),
    ('Van', 'Van'),
    # Add more categories as needed
]

# Choices for vehicle value categories
VALUE_CATEGORIES_CHOICES = [
    ('Highest value', 'Highest value'),
    ('High Value', 'High Value'),
    ('Medium Value', 'Medium Value'),
    ('Low Value', 'Low Value'),
    ('Very Low Value', 'Very Low Value'),
]

class Vehicle(models.Model):
    industry = models.CharField(max_length=100, choices=INDUSTRY_CHOICES)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=VEHICLE_CATEGORY_CHOICES)
    date_registered = models.DateField()
    date_manufactured = models.DateField()
    location = models.CharField(max_length=100)
    malfunction_date = models.DateField(blank=True, null=True)
    accident_records = models.TextField(blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    documentation = models.FileField(upload_to='vehicle_documents/')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE) #changes
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class VehicleDocument(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    document = models.FileField(upload_to='vehicle_documents/')
    description = models.TextField()

class ConcernedPeople(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=100)

class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE) #changes

class PurchaseRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    purchase_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.CharField(max_length=100)
    receipt = models.FileField(upload_to='purchase_records/')

class WarrantyRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    provider = models.CharField(max_length=100)
    terms_conditions = models.TextField()

class RepairRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    repair_date = models.DateField()
    details = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    technician = models.CharField(max_length=100)
    receipt = models.FileField(upload_to='repair_records/')

# Other models such as contract management, investments, fixed assets, etc. can be added similarly

# Sorting options with verbose names
SORT_OPTIONS = {
    'category': _('Category'),
    'date_created_asc': _('Date Created (Ascending)'),
    'date_created_desc': _('Date Created (Descending)'),
    'date_modified_asc': _('Date Modified (Ascending)'),
    'date_modified_desc': _('Date Modified (Descending)'),
    'expiry_date_warranty_asc': _('Expiry Date of Warranty (Ascending)'),
    'expiry_date_warranty_desc': _('Expiry Date of Warranty (Descending)'),
    'service_date_asc': _('Service Date (Ascending)'),
    'service_date_desc': _('Service Date (Descending)'),
    'repair_dates_asc': _('Repair Dates (Ascending)'),
    'repair_dates_desc': _('Repair Dates (Descending)'),
    'date_manufactured_asc': _('Date of Manufacture (Ascending)'),
    'date_manufactured_desc': _('Date of Manufacture (Descending)'),
}

## Models for Asset Selling and Leasing using Blockchain (to be implemented)

class AssetTransaction(models.Model):
    asset = models.ForeignKey(InventoryItem, on_delete=models.CASCADE) 
    seller = models.ForeignKey(CustomUser, related_name='sales', on_delete=models.CASCADE) 
    buyer = models.ForeignKey(CustomUser, related_name='purchases', on_delete=models.CASCADE) 
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    currency = models.CharField(max_length=3) 
    date = models.DateTimeField(auto_now_add=True) 
    is_leased = models.BooleanField(default=False)
