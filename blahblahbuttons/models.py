from django.db import models
from shop.models.productmodel import Product
from django.db import models

class Buttons(Product):
    size = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.IntegerField()
    photo = models.ImageField(upload_to='product_photo',
                            blank=True)

    class Meta: pass