from django.shortcuts import render

def index(request):
    file = 'sito_tesina/index.html'
    return render(request,file)

