from django.shortcuts import render

def index(request):
    file = 'stazioni_meteo/index.html'
    return render(request,file)

