from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import InventoryItem, Expense, IntangibleAsset, Machinery, HardwareSoftware, Furniture, Investment, FixedAsset, Contract

CustomUser = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        email = validated_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError("This email address is already in use.")
        
        user = CustomUser.objects.create_user(
            email=email,
            username=validated_data['username'],
            password=validated_data['password']
        )
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
        model = HardwareSoftware
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