from django.shortcuts import render

rooms = [
    {'id':1, 'name': 'lets learn python'},
    {'id':2, 'name': 'c++ tutorials'},
    {'id':3, 'name': 'TensorFlow'},
]

def home(request):
    return render(request, 'home.html', {'rooms':rooms})

def room(request):
    return render(request, 'room.html')
