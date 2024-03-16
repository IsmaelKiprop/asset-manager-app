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