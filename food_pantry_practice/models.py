from django.db import models

# Create your models here.


class FoodBank(models.Model):
    name = models.CharField(max_length=500)
    state = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    contact_info = models.CharField(max_length=500)
    website = models.CharField(max_length=500)

    def __str__(self):
        return self.name
