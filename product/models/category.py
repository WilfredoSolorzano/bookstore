#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True)  # 👈 Campo que está faltando no banco
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
