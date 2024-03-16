from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import binascii
import os

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email=email, username=username, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class AuthToken(models.Model):
    key = models.CharField(max_length=40, primary_key=True)
    user = models.ForeignKey(CustomUser, related_name='auth_tokens', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(AuthToken, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key

# Models for Inventory Management

from django.db import models

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
    
    # Other fields and functionalities can be added as needed

class Expense(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField()
    category = models.CharField(max_length=100, choices=EXPENSE_CATEGORIES_CHOICES)

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()

class BankConnection(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    routing_number = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

class VAT(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    vat_number = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=5, decimal_places=2)

class Report(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    report_type = models.CharField(max_length=100)
    content = models.TextField()

class Employee(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=100)

class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=50)

class Transaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField()
    recurring = models.BooleanField(default=False)

class Inventory(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class Project(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2)

class Budget(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    manager = models.ForeignKey('CustomUser', on_delete=models.CASCADE)  # Assuming CustomUser model exists

    # Other fields and functionalities can be added as needed

class StockReturn(models.Model):
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    return_reason = models.TextField()
    return_date = models.DateField()

    # Other fields and functionalities can be added as needed

class StockRequest(models.Model):
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    requested_quantity = models.PositiveIntegerField()
    request_date = models.DateField()
    requester = models.ForeignKey('CustomUser', on_delete=models.CASCADE)  # Assuming CustomUser model exists


# Models for Intangible Assets

class IntangibleAsset(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    expiration_date = models.DateField()
    document = models.FileField(upload_to='intangible_assets/')

# Models for Machinery and Vehicles

class Machinery(models.Model):
    name = models.CharField(max_length=100)
    warranty_information = models.TextField()
    service_history = models.TextField()
    location = models.CharField(max_length=100)

# Models for Hardware and Software

class HardwareSoftware(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    warranty_information = models.TextField()
    repair_history = models.TextField()

# Models for Furniture

class Furniture(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    warranty_information = models.TextField()
    repair_history = models.TextField()

# Models for Investments

class Investment(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)  # Multicurrency support

# Models for Fixed Assets

class FixedAsset(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    warranty_information = models.TextField()
    service_history = models.TextField()
    location = models.CharField(max_length=100)

# Models for Contract Management

class Contract(models.Model):
    category = models.CharField(max_length=100)
    expiration_date = models.DateField()
    document = models.FileField(upload_to='contracts/')

# Models for Finance Management

class Savings(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField()

class Budget(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

class Bill(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    paid = models.BooleanField(default=False)
    description = models.TextField()

class FinancialReport(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    report_type = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

# Models for Company Details

class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    number_of_employees = models.PositiveIntegerField()
    industry = models.CharField(max_length=100)

# Models for Chat Functionality

class ChatMessage(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name='received_messages', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

# Models for Multicurrency Valuation

class Valuation(models.Model):
    asset = models.OneToOneField('Asset', on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

# Models for Asset Management

class Asset(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='asset_photos/')

# Models for Gantt Charts and Analytics

class Analytics(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    completion_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    milestone_reached = models.BooleanField(default=False)
    tasks_completed = models.PositiveIntegerField(default=0)
    total_tasks = models.PositiveIntegerField(default=0)
    revenue_generated = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    expenses_incurred = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    efficiency_score = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    customer_satisfaction = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    net_profit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # Add more fields as needed


# Models for Asset Selling and Leasing using Blockchain (to be implemented)
class AssetTransaction(models.Model):
    asset = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    seller = models.ForeignKey(CustomUser, related_name='sales', on_delete=models.CASCADE)
    buyer = models.ForeignKey(CustomUser, related_name='purchases', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    date = models.DateTimeField(auto_now_add=True)
    is_leased = models.BooleanField(default=False)