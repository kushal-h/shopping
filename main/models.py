from django.db import models

# Create your models here.
class products :
    name : str
    img : str
    desc : str
    price : float


class selling(models.Model):
    price = models.FloatField(max_length=10)
    products_name = models.CharField(max_length=50)
    products_image = models.CharField(max_length=100, null = True)
