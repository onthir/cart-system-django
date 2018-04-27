from django.db import models
from django.conf import settings
from products.models import Product

User = settings.AUTH_USER_MODEL

# create the model manager for cart system       

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    products = models.ManyToManyField(Product, blank=True)
    total = models.FloatField(default=0.0)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.timestamp)