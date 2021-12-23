from django.db import models


class ProductCategory(models.Model):
    """ Product Category Model """
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        """ String Representation of object"""
        return str(self.name)


class Product(models.Model):
    """ Product Model """
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name="Product")
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    cover_image = models.ImageField()
    sku = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        """ String Representation of object"""
        return str(self.name)


class ProductImages(models.Model):
    """ Product can have multiple images """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()
    status = models.BooleanField(default=True)

    def __str__(self):
        """ String Representation of object"""
        return str(self.product)