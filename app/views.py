from django.shortcuts import render, redirect
from .models import Colori
from .forms import ColoriForm

# Create your views here.

def index(request):
    form = ColoriForm()
    if request.GET.get('errore') == 'esiste già':
        return render(request,'app/index.html', {'form':form,'colori': Colori.objects.all(),'errore':'Esiste già'})
    else:
        return render(request,'app/index.html', {'form':form,'colori': Colori.objects.all()})

def aggiungi(request):
    codice = request.POST.get('codice')
    colore = ""
    for c in Colori.objects.all():
        if c.codice == codice:
            return redirect('/app?errore=esiste+già')
    for posizione in range(len(request.POST.get('colore'))):
        if posizione == 0:
            colore += colore[posizione].upper()
        else:
            colore += colore[posizione].lower()
    NuovoColore = Colori(codice ='#'+codice, colore = colore2)
    NuovoColore.save()
    return redirect('/app/')

def cancella(request, codice):
    Colori.objects.filter(codice='#'+codice).delete()
    return redirect('/app/')