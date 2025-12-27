from django.db import models
from django.contrib.auth.models import User
from product.models import Product


class Order(models.Model):
    product: models.ManyToManyField[Product, models.Model] = models.ManyToManyField(Product, blank=False)
    user: models.ForeignKey[User] = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity: models.IntegerField = models.IntegerField(default=1)
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"
