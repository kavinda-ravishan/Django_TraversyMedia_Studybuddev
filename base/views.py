from django.shortcuts import render

rooms = [
    {'id':1, 'name': 'lets learn python'},
    {'id':2, 'name': 'c++ tutorials'},
    {'id':3, 'name': 'TensorFlow'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request):
    return render(request, 'base/room.html')
