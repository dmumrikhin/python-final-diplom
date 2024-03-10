from rest_framework import serializers

from backend.models import Category, Contact, Product, ProductInfo, ProductParameter, Shop, User

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'user', 'state',)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'category',)

class ProductParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductParameter
        fields = ('id', 'parameter', 'value',)

class ProductInfoSerializer(serializers.ModelSerializer):
    product_parameters = ProductParameterSerializer(many=True)

    class Meta:
        model = ProductInfo
        fields = ('id', 'model', 'product', 'shop', 'quantity', 'price', 
                  'price_rrc', 'product_parameters',)
        




