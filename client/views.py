from django.shortcuts import render
from .models import Client_Data

# Create your views here.

def index(request):
    clients = Client_Data.objects.all()
    context = {
        'clients': clients,
    }
    return render(request, 'client/index.html', context)
