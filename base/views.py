from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)

    context = {'room': room}
    return render(request, 'base/room.html', context)


def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        # print(request.POST), print(request.POST.get('name'))
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') # name value of url ( path('', views.home, name='home') )

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):

    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room) # (instance = room) : form will pre filled with room (room with pk)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room) # instance = room : update the room
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}

    return render(request, 'base/room_form.html', context) 