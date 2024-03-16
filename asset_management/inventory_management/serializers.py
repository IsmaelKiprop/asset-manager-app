from rest_framework import serializers
from django.contrib.auth import get_user_model

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