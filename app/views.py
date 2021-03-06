from django.shortcuts import render, redirect
from .models import Colori,Lista
from .forms import ColoriForm,ListaForm

# Create your views here.

def index(request):
    form = ColoriForm()
    if request.GET.get('errore') == 'esiste già':
        return render(request,'app/index.html', {'form':form,'colori': Colori.objects.all(),'errore':'Esiste già'})
    elif request.POST.get('colore'):
        return render(request,'app/index.html', {'form':form,'colori': cerca(request)})
    else:
        return render(request,'app/index.html', {'form':form,'colori': Colori.objects.all()})
def aggiungi(request):
    codice = request.POST.get('codice').lower()
    colore = ""
    for c in Colori.objects.all():
        if c.codice == codice:
            return redirect('/app?errore=esiste+già')
    for posizione in range(len(request.POST.get('colore'))):
        if posizione == 0:
            colore += request.POST.get('colore')[posizione].upper()
        else:
            colore += request.POST.get('colore')[posizione].lower()
    NuovoColore = Colori(codice = codice, colore = colore)
    NuovoColore.save()
    return redirect('/app/')

def cerca(request):
    colore = ""
    for posizione in range(len(request.POST.get('colore'))):
        if posizione == 0:
            colore += request.POST.get('colore')[posizione].upper()
        else:
            colore += request.POST.get('colore')[posizione].lower()
    if colore:
        select = Colori.objects.filter(colore__startswith=colore)
        return select
    return Colori.objects.all()

def cancella(request, codice):
    Colori.objects.filter(codice='#'+codice).delete()
    return redirect('/app/')

def lista(request):
    if request.POST:
        NuovoComando = Lista(testo = request.POST.get('testo'))
        NuovoComando.save()
    return render(request,'app/lista.html',{'lista':Lista.objects.all(),'form':ListaForm()})





    
