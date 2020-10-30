# -*- coding: utf-8 -*-

from django.db import models


class Shop(models.Model):

    name = models.CharField(max_length=50)


class Article(models.Model):

    shop = models.ForeignKey(
        Shop,
        related_name='articles',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50)
    price = models.FloatField()
