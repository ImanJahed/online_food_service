# Generated by Django 5.0 on 2023-12-16 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_rename_shipping_cost_transactionorder_shipping_cost_admin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('INITIAL', 'INITIAL'), ('PAPERING', 'PAPERING'), ('SENDING', 'SENDING'), ('CANCELED', 'CANCELED')], default='INITIAL', max_length=50),
        ),
    ]