from django.shortcuts import render
from .models import Colori
from .forms import ColoriForm

# Create your views here.

def index(request):
    form = ColoriForm()
    if request.method == 'GET':
        return render(request,'app/index.html', {'form':form,'colori': Colori.object.all()})
    else:
        return render(request,'app/index.html', {'form':form , 'colori': Colori.object.all()})