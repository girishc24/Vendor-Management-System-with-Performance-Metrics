# Generated by Django 4.2.7 on 2023-12-04 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0006_alter_purchaseorder_delivery_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('canceled', 'Canceled')], default='Completed', max_length=9),
        ),
    ]
