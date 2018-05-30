from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'giochi/index.html')

def tower_block(request):
    return render(request, 'giochi/tower-block.html')