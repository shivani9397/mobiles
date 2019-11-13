from django.db import models

# Create your models here.


class Samsung(models.Model):
    mname = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    price = models.FloatField()
    qty = models.IntegerField()
    reviews = models.CharField(max_length=100)
    class Meta:
        db_table = 'Samsung'