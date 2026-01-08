from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Event, Registration
from .forms import EventForm
from django.http import HttpResponse
# Create your views here.
def home(request):
    events = Event.objects.all()
    return HttpResponse("Welcome to Event Management System")

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event =form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('home')
    else:
            form = EventForm()
    return render(request, 'events/create_events.html', {'form':form})

@login_required
def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    Registration.objects.get_or_create(user=request.user, event=event)
    return redirect('home')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})