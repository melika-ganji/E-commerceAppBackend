from django.contrib import admin
from django.contrib.admin import register

from product.models import Product, ProductAttributeValue, ProductAttribute, ProductType, Category, Brand


@register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'get_productType_id', 'upc', 'brand', 'category', 'price', 'description')
    list_filter = ('productType', 'upc', 'brand', 'category')

    search_fields = ('upc',)
    ordering = ('price',)

    def get_productType_id(self, obj):
        return obj.productType.id

    get_productType_id.short_description = 'Product Type ID'


@register(ProductAttributeValue)
class ProductAttributeValueAdmin(admin.ModelAdmin):
    model = ProductAttributeValue
    list_display = ('product', 'productAttribute', 'value')
    search_fields = ('value',)
    ordering = ('product',)


@register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    model = ProductAttribute
    list_display = ('productType', 'name')
    search_fields = ('name',)
    ordering = ('productType',)


@register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('id', 'parent', 'name')
    search_fields = ('name',)
    ordering = ('name',)


@register(Brand)
class BrandAdmin(admin.ModelAdmin):
    model = Brand
    list_display = ('id', 'parent', 'name')
    search_fields = ('name',)
    ordering = ('name',)


