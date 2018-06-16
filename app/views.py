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
        if metodo == "Inserisci":  #se si vuole inserire un colore
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
    else:
        return render(request,'app/index.html', {'form':form,'colori': Colori.objects.all()})