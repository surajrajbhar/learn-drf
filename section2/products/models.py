from django.db import models

# Create your models here.


class Manufacturers(models.Model):
    name =  models.CharField(max_length=100)
    location  = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    manufacture =  models.ForeignKey(Manufacturers , on_delete=  models.CASCADE, related_name="products")
    name =  models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    photo  =  models.ImageField(blank=True, null=True)
    price  =  models.FloatField()
    shipping_cost = models.FloatField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    