from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.title


class Cuisine(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.title


SPICY_LEVEL_CHOICES = (
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


class Restaurant(models.Model):
    title = models.CharField(
        max_length=255, unique=True, blank=False, null=False)

    def __str__(self):
        return self.title


class Menu_item(models.Model):
    title = models.CharField(
        max_length=255, unique=True, blank=False, null=False)
    description = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    spicy_level = models.IntegerField(choices=SPICY_LEVEL_CHOICES)
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + f' ({self.restaurant})'
