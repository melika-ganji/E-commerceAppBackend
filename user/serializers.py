from rest_framework import serializers

from user.models import CustomUser, AccountUser


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class CreateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountUser
        fields = '__all__'
