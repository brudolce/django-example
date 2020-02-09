from django.db import models


class Produto(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TimeField()

    def __str__(self):
        return self.name
