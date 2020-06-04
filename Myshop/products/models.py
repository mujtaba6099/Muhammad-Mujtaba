from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=2083)


class Offer(models.Model):
    code=models.IntegerField()
    description=models.CharField(max_length=255)
    discount=models.FloatField()