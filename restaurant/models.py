from django.db import models

from accounts.models import Restaurant


# Create your models here.

def restaurant_image_path(instance, filename):
    return f'{instance.vendor.name}/food/{filename}'


class Category(models.Model):
    vendor = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def clean(self):
        self.category_name = self.category_name.capitalize()

    def __str__(self):
        return self.category_name


class Food(models.Model):
    vendor = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    food_title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=250, blank=True)
    price = models.PositiveIntegerField()
    preparation_time = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to=restaurant_image_path)

    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.food_title
