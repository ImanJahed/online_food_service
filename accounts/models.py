from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    ROLL = (
        (1, 'Customer'),
        (2, 'Restaurant')
    )
    roll = models.PositiveSmallIntegerField(choices=ROLL, blank=True, null=True)

    def __str__(self):
        return self.username


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    address = models.TextField()

    def __str__(self):
        return self.user.username


class Restaurant(models.Model):
    RESTAURANT_TYPE = (
        ('Fast Food', 'Fast Food'),
        ('Traditional Food', 'Traditional Food')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='restaurant')
    name = models.CharField(max_length=50)
    restaurant_type = models.CharField(max_length=20, choices=RESTAURANT_TYPE)
    start_time = models.TimeField()
    finish_time = models.TimeField()
    shipping_time = models.IntegerField()
    shipping_cost = models.PositiveIntegerField(default=0, null=True, blank=True)
    restaurant_cover = models.ImageField(upload_to='restaurant_img', null=True, blank=True)

    def __str__(self):
        return self.name


