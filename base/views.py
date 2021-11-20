from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

rooms = [
    {'id': 1, 'name': 'lets learn python'},
    {'id': 2, 'name': 'lets learn '},
    {'id': 3, 'name': 'lets '},

]


def home(request):
    return render(request, 'home.html', {'rooms': rooms})


def room(request):
    return HttpResponse('ROOM')
