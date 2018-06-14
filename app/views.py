from django.shortcuts import render
from .models import Colori
from .forms import ColoriForm

# Create your views here.

def index(request):
    form = ColoriForm()
    colori = Colori.objects.all()
    if request.method == 'POST':
        codice = request.POST['codice'].lower()
        colore = ""
        for colore in colori:
            if colore.codice == codice:
                 return render(request,'app/index.html', {'form':form,'colori': colori,'errore':'Esiste già'})
        for posizione in range(len(request.POST['colore'])):
            if posizione == 0:
                colore += request.POST['colore'][posizione].upper()
            else:
                colore += request.POST['colore'][posizione].lower()
        NuovoColore = Colori(codice = codice, colore = colore)
        NuovoColore.save()
        return render(request,'app/index.html', {'form':form,'colori': colori})
    else:
        return render(request,'app/index.html', {'form':form , 'colori': colori})