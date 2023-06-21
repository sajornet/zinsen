from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name


class Provider(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Offering(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    logo = models.CharField(max_length=300)
    description = models.TextField(max_length=1000)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    minimum = models.CharField(max_length=30, null=True, blank=True)
    maximum = models.CharField(max_length=30, null=True, blank=True)
    minimum_term = models.CharField(max_length=30, null=True, blank=True)
    maximum_term = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name
    

