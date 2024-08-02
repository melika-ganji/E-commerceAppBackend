from django.contrib import admin
from django.contrib.admin import register

from .models import CustomUser, AccountUser


@register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ('username', 'phoneNumber', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password', 'phoneNumber')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'phoneNumber', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('username', 'phoneNumber')
    ordering = ('username',)


@register(AccountUser)
class AccountUserAdmin(admin.ModelAdmin):
    model = AccountUser
    list_display = ('get_user_id', 'get_username', 'name', 'lastName', 'email', 'address')
    search_fields = ('user__username', 'email')
    ordering = ('user__username',)

    def get_user_id(self, obj):
        return obj.user.id

    def get_username(self, obj):
        return obj.user.username

    get_user_id.short_description = 'User ID'
    get_username.short_description = 'Username'
