from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=30)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subBrands', null=True, blank=True)

    def __str__(self):
        return f"{self.name} from {self.parent}"


class Category(models.Model):
    name = models.CharField(max_length=30)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subCategory', null=True, blank=True)

    def __str__(self):
        return f"{self.name} from {self.parent}"


class ProductType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ProductAttribute(models.Model):
    name = models.CharField(max_length=30)
    productType = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='attributes')

    def __str__(self):
        return f"{self.name} for {self.productType}"


class Product(models.Model):
    name = models.CharField(max_length=30)
    productType = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='products')
    upc = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField(blank=True)
    price = models.IntegerField()


class ProductAttributeValue(models.Model):
    value = models.CharField(max_length=30)
    productAttribute = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE, related_name='values')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='values')

    def __str__(self):
        return f"for {self.product} => {self.productAttribute} = {self.value}"
