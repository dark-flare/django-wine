from django.db import models
from datetime import datetime
# Create your models here.


class Nation(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Winemaker(models.Model):
    name = models.CharField(max_length=200)
    nationality = models.ForeignKey(Nation, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Variety(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Wine(models.Model):
    name = models.CharField(max_length=400)
    url = models.CharField(max_length=200)
    image_url = models.CharField(max_length=400)
    quantity = models.IntegerField(default=0)
    consumed = models.IntegerField(default=0)
    comments = models.TextField(max_length=2000, blank=True)
    score = models.FloatField(default=0)
    price = models.FloatField()
    abv = models.FloatField()
    last_stock_date = models.DateTimeField(null=True, blank=True)
    last_drank_date = models.DateTimeField(null=True, blank=True)
    winemaker = models.ForeignKey(Winemaker, on_delete=models.PROTECT)
    nation = models.ForeignKey(Nation, on_delete=models.PROTECT)
    variety = models.ForeignKey(Variety, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name