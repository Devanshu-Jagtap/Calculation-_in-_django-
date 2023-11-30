from django.db import models

# Create your models here.
class additions(models.Model):
    Value1 = models.IntegerField()
    Value2 = models.IntegerField()
    result = models.IntegerField()

class subtractions(models.Model):
    Value1 = models.IntegerField()
    Value2 = models.IntegerField()
    result = models.IntegerField()

class multiplications(models.Model):
    Value1 = models.IntegerField()
    Value2 = models.IntegerField()
    result = models.IntegerField()

class divisions(models.Model):
    Value1 = models.IntegerField()
    Value2 = models.IntegerField()
    result = models.IntegerField()