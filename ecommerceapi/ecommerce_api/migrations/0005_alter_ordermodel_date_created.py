# Generated by Django 5.2.4 on 2025-07-07 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_api', '0004_remove_ordermodel_completed_ordermodel_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
