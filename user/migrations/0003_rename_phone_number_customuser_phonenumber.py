# Generated by Django 4.2 on 2024-08-02 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_customuser_email_accountuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='phone_number',
            new_name='phoneNumber',
        ),
    ]
