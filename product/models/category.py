from django.db import models


class Category(models.Model):
    title: models.CharField = models.CharField(max_length=100)
    description: models.TextField = models.TextField(blank=True, null=True)
    slug: models.SlugField = models.SlugField(unique=True)
    active: models.BooleanField = models.BooleanField(default=True)

    def __str__(self):
        return self.title
