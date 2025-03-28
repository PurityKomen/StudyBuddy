from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request,'base/home.html',context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request,'base/room.html',context)

def createRoom(request):
    context = {}
    return render(request,'base/room_form.html',context)
