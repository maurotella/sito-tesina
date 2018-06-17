from django.shortcuts import render, redirect
from .models import Colori
from .forms import ColoriForm

# Create your views here.

def index(request):
    form = ColoriForm()
    if request.method == 'POST':
        colore = ""
        metodo = request.POST['metodo']
        if metodo == "Inserisci":  #se si vuole inserire un colore
            codice = request.POST['codice'].lower()
            for c in Colori.objects.all():
                if c.codice == codice:
                    return render(request,'app/index.html', {'form':form,'colori': Colori.objects.all(),'errore':'Esiste già'})
            for posizione in range(len(request.POST['colore'])):
                if posizione == 0:
                    colore += request.POST['colore'][posizione].upper()
                else:
                    colore += request.POST['colore'][posizione].lower()
            NuovoColore = Colori(codice = codice, colore = colore)
            NuovoColore.save()
            return render(request,'app/index.html', {'form':form,'colori': Colori.objects.all()})  #invia la lista di tutti i colori
        if metodo == "Ricerca":  #se si vuole cercare un colore
            colori = []        
            if len(request.POST['colore']) >= 1:
                for posizione in range(len(request.POST['colore'])):
                    if posizione == 0:
                        colore += request.POST['colore'][posizione].upper()
                    else:
                        colore += request.POST['colore'][posizione].lower()
                colori = Colori.objects.filter(colore__startswith = colore)  # lista dei colori che si chiamano come quelli cercati
                return render(request,'app/index.html', {'form':form,'colori': colori})
            return render(request,'app/index.html', {'form':form,'colori': Colori.objects.all()})
    else:
        return render(request,'app/index.html', {'form':form,'colori': Colori.objects.all()})


def cancella(request, codice):
    Colori.objects.filter(codice='#'+codice).delete()
    