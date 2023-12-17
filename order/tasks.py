from celery import shared_task, chord
from django.utils import timezone
from datetime import timedelta
from order.models import Order


# @shared_task
# def change_to_preparation(order_id):
#     try:
#         order = Order.objects.get(pk=order_id)
#         if order.status == 'Initial':
#             order.status = 'Papering'
#             order.save()
#     except Order.DoesNotExist:
#         pass

#
# @shared_task
# def change_to_canceled(order_id):
#     try:
#         order = Order.objects.get(pk=order_id)
#         if order.status == 'Papering':
#             order.status = 'Canceled'
#             order.save()
#     except Order.DoesNotExist:
#         pass
#
#
# def schedule_order_tasks(instance_id):
#     instance = Order.objects.get(pk=instance_id)
#     now = timezone.now()
#     time_difference = now - instance.order_time
#     if time_difference >= timedelta(seconds=15):
#         print('Hello')
#         change_to_preparation.apply_async(args=[instance.id], countdown=40)
#
#     if time_difference >= timedelta(seconds=20):
#         change_to_canceled.apply_async(args=[instance.id], countdown=60)













@shared_task
def change_to_preparation(order_id):
    try:
        order = Order.objects.get(pk=order_id)

        if order.status == 'Initial':
            print(1)
            now = timezone.now()
            time_difference = now - order.order_time
            if time_difference >= timedelta(seconds=15):
                print(2)
                order.status = 'Papering'
                order.save()
    except Order.DoesNotExist:
        pass


@shared_task
def change_to_canceled(order_id):
    try:
        order = Order.objects.get(pk=order_id)
        if order.status == 'Papering':
            now = timezone.now()
            time_difference = now - order.order_time
            if time_difference >= timedelta(seconds=20):
                order.status = 'Canceled'
                order.save()
    except Order.DoesNotExist:
        pass
