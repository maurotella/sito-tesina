from django.shortcuts import render
from django.http import HttpResponse
from . models import Classifica

# Create your views here.

def index(request):
    return render(request, 'giochi/index.html')

def tower_block(request):
    return render(request, 'giochi/tower_block.html')

def gioco2048(request):
    return render(request, 'giochi/2048.html')

def risultato(request,gioco,risultato):
    if request.method == 'GET':
        if gioco:
            new_risultato = Classifica(gioco=gioco, risultato=risultato, user="anonimo")
            new_risultato.save()
        return HttpResponse("Fatto")

def carica_classifica(request,gioco):
    if gioco == '2048':    
        classifica = Classifica.objects.filter(gioco="2048").order_by('-risultato') 
    return render(request,'giochi/classifica.html', {'gioco':gioco, 'classifica':classifica})

    
