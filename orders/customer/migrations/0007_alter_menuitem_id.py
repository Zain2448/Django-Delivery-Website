# Generated by Django 5.1.4 on 2025-01-07 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_alter_menuitem_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
