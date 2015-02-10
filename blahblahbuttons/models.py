from django.db import models
from shop.models import Product
from django.db import models

class Buttons(Product):
    description = models.TextField()
    amount = models.IntegerField()
    photo = models.ImageField(upload_to='product_photo',
                            blank=True)

    class Meta:
        verbose_name_plural = "buttons"

