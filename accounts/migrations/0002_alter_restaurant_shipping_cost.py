# Generated by Django 5.0 on 2023-12-16 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='shipping_cost',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]