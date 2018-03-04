from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Pet

def home(request):
    pets = Pet.objects.all()
    return render(request,'home.html', {'pets': pets})

def pet_detial(request, id):
    try:
        pet = Pet.objects.get(id=id)
    except DoesNotExist:
        raise Http404('pet not found')
    return render('pet_detail.html', {'pet': pet})
