from rest_framework import serializers

from product.models import Brand, Category, ProductType, Product, ProductAttribute


class SimpleBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']


class BrandSerializer(serializers.ModelSerializer):
    parent = SimpleBrandSerializer(read_only=True)
    parentName = serializers.CharField(write_only=True, required=False, allow_null=True)

    class Meta:
        model = Brand
        fields = '__all__'

    def create(self, validated_data):
        parentName = validated_data.pop('parentName', None)
        if parentName:
            parent = Brand.objects.filter(name=parentName).first()
            if parent:
                validated_data['parent'] = parent
            else:
                raise serializers.ValidationError({f'{parentName}': 'Parent brand with this name does not exist.'})
        return super().create(validated_data)

    def update(self, instance, validated_data):
        parentName = validated_data.pop('parent_name', None)
        if parentName:
            parent = Brand.objects.filter(name=parentName).first()
            if parent:
                validated_data['parent'] = parent
            else:
                raise serializers.ValidationError({f'{parentName}': 'Parent brand with this name does not exist.'})
        return super().update(instance, validated_data)


class SimpleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    parent = SimpleCategorySerializer(read_only=True)
    parentName = serializers.CharField(write_only=True, required=False, allow_null=True)

    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        parentName = validated_data.pop('parentName', None)
        if parentName:
            parent = Category.objects.filter(name=parentName).first()
            if parent:
                validated_data['parent'] = parent
            else:
                raise serializers.ValidationError({f'{parentName}': 'Parent category with this name does not exist.'})
        return super().create(validated_data)

    def update(self, instance, validated_data):
        parentName = validated_data.pop('parent_name', None)
        if parentName:
            parent = Category.objects.filter(name=parentName).first()
            if parent:
                validated_data['parent'] = parent
            else:
                raise serializers.ValidationError({f'{parentName}': 'Parent category with this name does not exist.'})
        return super().update(instance, validated_data)


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'


class ProductAttributeSerializer(serializers.ModelSerializer):
    productTypeName = serializers.CharField(write_only=True, required=True)
    productType = ProductTypeSerializer(read_only=True)

    class Meta:
        model = ProductAttribute
        fields = '__all__'

    def create(self, validated_data):
        productTypeName = validated_data.pop('productTypeName', None)
        if productTypeName:
            productType = ProductType.objects.filter(name=productTypeName).first()
            if productType:
                validated_data['productType'] = productType
            else:
                raise serializers.ValidationError({f'{productTypeName}': 'Product Type with this name does not exist.'})
        print(validated_data)
        return super().create(validated_data)


