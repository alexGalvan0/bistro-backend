from django.db import models

# Create your models here.


class Menu_item(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=3, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Category(models.Model):
    title = models.CharField(max_length=255)


class Cuisine(models.Model):
    title = models.CharField(max_length=255)
