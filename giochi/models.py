from django.db import models

# Create your models here.

class Classifica(models.Model):
    risultato = models.IntegerField()
    gioco = models.CharField(max_length=30, default="")
    data = models.DateTimeField(auto_now=True)