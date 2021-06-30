from products.models import Product, Category
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    #producto_categoria = serializers.CharField(read_only=True, source="category.name")
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source="category")
    name = serializers.CharField(required=True, min_length=3)
    
    def validate_nombre (self, value):
        existe = Product.objects.filter(name=value).exists()
        if existe:
            raise serializers.ValidationError("Este producto ya existe")
        return value
    
    class Meta:
        model = Product
        fields = '__all__'