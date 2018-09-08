from django.db import models

# Create your models here.

class Colori(models.Model):
    codice = models.CharField(max_length=7, primary_key=True)
    colore = models.CharField(max_length=30)

    def __str__(self):
        return self.colore + " | " + self.codice
    
   
class Lista(models.Model):
    testo = models.CharField(max_length=500)
    
