from django.shortcuts import render
from .models import Colori
from .forms import ColoriForm

# Create your views here.

def index(request):
    form = ColoriForm()
    if request.method == 'POST':
        codice = request.POST['codice'].lower()
        colore = ""
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
    elif request.method == 'GET':
        codice = request.GET.get('codice')
        colore = ""
        for posizione in range(len(request.POST.get('colore'))):
            if posizione == 0:
                colore += request.POST['colore'][posizione].upper()
            else:
                colore += request.POST['colore'][posizione].lower()
        select = Colori.object.filter(colore__startswith=colore, codice__startswith=codice)
        return render(request,'app/index.html', {'form':form,'colori': Colori.objects.all(),'select':select})
    else:
        return render(request,'app/index.html', {'form':form,'colori': Colori.objects.all()})