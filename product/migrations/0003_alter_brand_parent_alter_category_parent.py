# Generated by Django 4.2 on 2024-08-10 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_brand_parent_alter_category_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subBrands', to='product.brand'),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subCategory', to='product.category'),
        ),
    ]
