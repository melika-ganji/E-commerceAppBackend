from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, phoneNumber=None, **extra_fields):
        if not username:
            raise ValueError("The Username field must be set")
        if not password:
            raise ValueError("The Password field must be set")
        if not phoneNumber:
            raise ValueError("The Phone Number field must be set")

        user = self.model(
            username=username,
            phoneNumber=phoneNumber,
            # email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, phoneNumber=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, phoneNumber, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    phoneNumber = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phoneNumber']

    def __str__(self):
        return self.username


class AccountUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="accounts")
    name = models.TextField(max_length=60)
    lastName = models.TextField(max_length=60)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return f"user {self.user} => {self.name} {self.lastName}"
