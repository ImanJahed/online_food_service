# Generated by Django 5.0 on 2023-12-15 17:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.IntegerField()),
                ('status', models.CharField(choices=[(1, 'PAPERING'), (2, 'SENDING'), (3, 'CANCEL')], max_length=50)),
                ('order_time', models.DateTimeField(auto_now_add=True)),
                ('shipping_cost', models.IntegerField()),
                ('auto_or_restaurant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.restaurant')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_food', to='restaurant.food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_order', to='accounts.customer')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_order', to='accounts.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_order', models.IntegerField()),
                ('shipping_cost', models.IntegerField()),
                ('restaurant_share', models.IntegerField()),
                ('admin_share', models.IntegerField()),
                ('total_restaurant_share', models.IntegerField()),
                ('total_admin_share', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='order.order')),
            ],
        ),
    ]
