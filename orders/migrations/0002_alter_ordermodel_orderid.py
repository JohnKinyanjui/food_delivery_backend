# Generated by Django 3.2.4 on 2021-07-01 23:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='orderId',
            field=models.UUIDField(auto_created=True, default=uuid.UUID('bf2587c2-6f07-4c7c-ae78-b2936d9fe155'), unique=True),
        ),
    ]