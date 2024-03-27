# Now let's update the serializers.py file:

from rest_framework import serializers
from .models import CustomUser, InventoryItem, Expense, IntangibleAsset, Machinery, ComputerHardware, ComputerSoftware, Furniture, Investment, FixedAsset, Contract, Savings, Budget, BankIntegration, Bill, FinancialGrowth

class CustomUserSerializer(serializers.ModelSerializer):
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'company_name', 'location', 'number_of_employees', 'industry', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

class IntangibleAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntangibleAsset
        fields = '__all__'

class MachinerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Machinery
        fields = '__all__'

class HardwareSoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComputerHardware
        fields = '__all__'

class HardwareSoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComputerSoftware
        fields = '__all__'

class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = '__all__'

class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = '__all__'

class FixedAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixedAsset
        fields = '__all__'

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

class SavingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savings
        fields = '__all__'

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'

class BankIntegrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankIntegration
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'

class FinancialReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialGrowth
        fields = '__all__'
