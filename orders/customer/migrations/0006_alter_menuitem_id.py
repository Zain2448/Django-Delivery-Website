# Generated by Django 5.1.4 on 2025-01-07 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_alter_ordermodel_is_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
