# Generated by Django 3.2.4 on 2021-07-01 23:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_productmodel_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='product_id',
            field=models.UUIDField(default=uuid.UUID('0adfb78a-258a-4523-8a45-e860de10884a'), unique=True),
        ),
    ]