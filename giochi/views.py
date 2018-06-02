from django.shortcuts import render
from . models import Classifica

# Create your views here.

def index(request):
    return render(request, 'giochi/index.html')

def tower_block(request):
    return render(request, 'giochi/tower_block.html')

def gioco2048(request):
    return render(request, 'giochi/2048.html')

def risultato(request):
    gioco = None
    risultato = None
    user = None
    if request.method == 'GET':
        gioco = request.GET['gioco']
        risultato = request.GET['risultato']
        user = request.GET['user']

    if gioco:
        new_risultato = Classifica(gioco=gioco, risultato=risultato, user=user)
        new_risultato.save()

    
