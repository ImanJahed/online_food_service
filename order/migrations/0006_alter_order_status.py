# Generated by Django 5.0 on 2023-12-17 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('INITIAL', 'Initial'), ('PAPERING', 'Papering'), ('SENDING', 'Sending'), ('CANCELED', 'Canceled')], default='INITIAL', max_length=50),
        ),
    ]
