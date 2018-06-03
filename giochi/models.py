from django.db import models

# Create your models here.

class Classifica(models.Model):
    risultato = models.IntegerField()
    gioco = models.CharField(max_length=30, default="")
    user = models.CharField(max_length=30, default="anonimo")
    data = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return(self.gioco + " | " + self.user + " : " + str(self.risultato)


