# -*- coding: utf-8 -*-

from django.db import models


class Shop(models.Model):

    name = models.CharField()


class Article(models.Model):

    shop = models.ForeignKey(Shop, related_name='articles')
    name = models.CharField()
    price = models.FloatField()
