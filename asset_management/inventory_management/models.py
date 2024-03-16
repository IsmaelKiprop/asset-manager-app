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

class InventoryItem(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)  # Multicurrency support
    photo = models.ImageField(upload_to='inventory_photos/')  # Upload photos

# Models for Expense Management

class Expense(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField()

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

class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=50)

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