# Generated by Django 5.0 on 2023-12-17 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Initial', 'Initial'), ('Papering', 'Papering'), ('Sending', 'Sending'), ('Canceled', 'Canceled')], default='Initial', max_length=50),
        ),
    ]
