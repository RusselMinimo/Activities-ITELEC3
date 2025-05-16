from rest_framework import serializers
from .models import Category, Product, Customer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'is_active']
        read_only_fields = ['created_at', 'updated_at']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'stock', 
                  'created_at', 'updated_at', 'is_available']
        read_only_fields = ['created_at', 'updated_at']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'address', 
                  'created_at', 'updated_at', 'is_active']
        read_only_fields = ['created_at', 'updated_at'] 