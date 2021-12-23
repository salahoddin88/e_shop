from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from datetime import datetime


class Order(models.Model):
    """ Order Model Class """
    ORDER_STATUS = (
        ('Pending', 'Pending'),
        ('In-progress', 'In-progress'),
        ('Delivered', 'Delivered'),
        ('canceled', 'canceled')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now())
    user_name = models.CharField(max_length=255)
    user_address = models.TextField()
    order_status = models.CharField(choices=ORDER_STATUS, max_length=255, default='Pending')
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        """ String Representation of object"""
        return f'{self.id} {self.order_status}'
    

class OrderDetails(models.Model):
    """ Order Details Model """
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        """ String Representation of object"""
        return f'{self.order.id} {self.product}'


class Reviews(models.Model):
    """ Review Model Class """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField()
    date = models.DateTimeField(default=datetime.now())
    status = models.BooleanField(default=True)

    def __str__(self):
        """ String Representation of object"""
        return f'{self.user} {self.product}'


class Payment(models.Model):
    """ Payment Model Class """
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=255)
    payment_id = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=255)

    def __str__(self):
        """ String Representation of object"""
        return str(self.transaction_id)


