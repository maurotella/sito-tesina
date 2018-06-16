from django.shortcuts import render
from .models import Colori
from .forms import ColoriForm

# Create your views here.

def index(request):
    form = ColoriForm()
    if request.method == 'POST':
        codice = request.POST['codice'].lower()
        colore = ""
        metodo = request.POST['metodo']
        if metodo == "Inserisci":
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
            return render(request,'app/index.html', {'form':form,'colori': Colori.objects.all()})
        if metodo == "Ricerca":
            colori = []
            if len(request.POST['colore']) >= 1:
                for posizione in range(len(request.POST['colore'])):
                    if posizione == 0:
                        colore += request.POST['colore'][posizione].upper()
                    else:
                        colore += request.POST['colore'][posizione].lower()
                colori = Colori.objects.filter(colore__startswith = colore)
            if codice:
                colori2 = []
                for c in Colori.objects.filter(codice__startswith = codice):
                    colori2.append(c)
                for colore in colori2:
                    if colore not in colori:
                        colori2.remove(colore)
                return render(request,'app/index.html', {'form':form,'colori': colori2})
            if len(request.POST['colore']) == 0 and not codice:
                return render(request,'app/index.html', {'form':form,'colori': colori})
    else:
        return render(request,'app/index.html', {'form':form,'colori': Colori.objects.all()})