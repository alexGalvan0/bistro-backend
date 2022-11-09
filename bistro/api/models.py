from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Cuisine(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


SPICY_LEVEL_CHOICES = (
    ('1',1),
    ('2',2),
    ('3',3),
    ('4',4),
    ('5',5),
)

class Menu_item(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    spicy_level = models.CharField(choices=SPICY_LEVEL_CHOICES, max_length=255)

    def __str__(self):
        return self.title
