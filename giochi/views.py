from django.shortcuts import render
from . models import Classifica

# Create your views here.

def index(request):
    return render(request, 'giochi/index.html')

def tower_block(request):
    return render(request, 'giochi/tower_block.html')

def gioco2048(request):
    classifica = Classifica.objects.filter(gioco="2048") 
    return render(request, 'giochi/2048.html', {'classifica':classifica})

def risultato(request,gioco,risultato):
    self.gioco = gioco
    self.risultato = risultato
    self.user = "anonimo"
    if request.method == 'GET':
        if gioco:
            new_risultato = Classifica(gioco=gioco, risultato=risultato, user=user)
            new_risultato.save()

    
