from django.db import models

# Create your models here.

class Classifica(models.Model):
    risultato = models.IntegerField()
    data = models.DateTimeField(auto_now=True)