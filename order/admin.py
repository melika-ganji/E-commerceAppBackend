from django.contrib import admin
from django.contrib.admin import register

from order.models import Basket


@register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_account_id', 'createdTime', 'modifiedTime', 'isActive')
    search_fields = ('id, get_account_id',)
    list_filter = ('get_account_id',)
    ordering = ('createdTime',)

    def get_account_id(self, obj):
        return obj.account.id

    get_account_id.short_description = "Account"


class BasketListAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_basket_id', 'get_product_id', 'quantity')
    search_fields = ('id, get_basket_id',)
    list_filter = ('get_basket_id',)
    ordering = ('id',)

    def get_product_id(self, obj):
        return obj.product.id

    def get_basket_id(self, obj):
        return obj.basket.id

    get_product_id.short_description = "Product"
    get_basket_id.short_description = "Basket"


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_account_id', 'get_basket_id', 'createdTime', 'status', 'totalAmount')
    search_fields = ('id', 'get_account_id', 'status')
    list_filter = ('id', 'status')
    ordering = ('createdTime',)

    def get_product_id(self, obj):
        return obj.product.id

    def get_basket_id(self, obj):
        return obj.basket.id

    get_product_id.short_description = "Product"
    get_basket_id.short_description = "Basket"
