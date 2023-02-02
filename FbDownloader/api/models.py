from django.db import models


# Create your models here.
class appmodel(models.Model):
    url = models.CharField(max_length=5000)
