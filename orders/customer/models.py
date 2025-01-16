from django.contrib.postgres.fields import ArrayField
from django.db import models

class MenuItem(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='menu_images/')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField('Category', related_name='items')


    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class OrderModel(models.Model):
    # Details about the order
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    items = models.ManyToManyField('MenuItem', related_name='order', blank=True)


    # Details about who ordered it
    name = models.CharField(max_length=100, blank = True)
    email = models.EmailField(blank = True)
    address = models.TextField(blank = True)
    postcode = models.CharField(max_length=10, blank = True)
    is_delivery = models.BooleanField(default=False, null = True)

    is_shipped = models.BooleanField(default=False, null = True)

    def __str__(self):
        return f'Order: {self.created_at.strftime("%d/%m/%Y, %H:%M:%S")}'