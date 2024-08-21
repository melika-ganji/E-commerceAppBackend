from django.db import models

from product.models import Product
from user.models import AccountUser


class Basket(models.Model):
    account = models.ForeignKey(AccountUser, on_delete=models.CASCADE, name='baskets')
    createdTime = models.DateTimeField(auto_now_add=True)
    modifiedTile = models.DateTimeField(auto_now=True, auto_now_add=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return f"The account {self.account} created the basket on {self.createdTime}"


class BasketList(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='basketLists')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='basketLists')
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"the {self.product} by {self.quantity} times adds to {self.basket}"


class Order(models.Model):
    account = models.ForeignKey(AccountUser, on_delete=models.CASCADE, related_name='orders')
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='orders')
    createdTime = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    totalAmount = models.FloatField(default=00.0)

    def __str__(self):
        return f"{self.account} ordered {self.basket} on {self.createdTime} with status={self.status}"
