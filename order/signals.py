from django.dispatch import receiver
from django.db.models.signals import post_save

from celery import chord
from .models import Order
from . import tasks


@receiver(post_save, sender=Order)
def schedule_order_tasks(sender, instance, created, **kwargs):
    if created:
        # تغییر وضعیت سفارش به "درحال آماده‌سازی" پس از 2 دقیقه
        tasks.change_to_preparation.apply_async(args=[instance.id], countdown=120)  # 120 ثانیه = 2 دقیقه

        # بررسی وضعیت سفارش و تغییر به "لغو شده" پس از 10 دقیقه
        chord(
            [tasks.change_to_preparation.s(instance.id)],
            tasks.change_to_canceled.s(instance.id)
        ).apply_async(countdown=600)  # 600 ثانیه = 10 دقیقه

































