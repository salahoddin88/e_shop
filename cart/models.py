from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Cart(models.Model):
    """ User Cart Model """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        """ String Representation of object"""
        return f'{self.user} {self.product}'