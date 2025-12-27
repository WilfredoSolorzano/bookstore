from django.db import models
from .category import Category


class Product(models.Model):
    title: models.CharField = models.CharField(max_length=100)
    description: models.TextField = models.TextField(max_length=500, blank=True, null=True)
    price: models.PositiveIntegerField = models.PositiveIntegerField(null=True)
    active: models.BooleanField = models.BooleanField(default=True)
    category: models.ManyToManyField[Category, models.Model] = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title
