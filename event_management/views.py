from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm  # Add this import
from .models import Event, Registration
from .forms import RegistrationForm

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_management/event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'event_management/event_detail.html', {'event': event})

@login_required
def register_event(request, event_id):
    print("INSIDE REGISTER EVENT FUNCTION")
    event = get_object_or_404(Event, pk=event_id)
    print("EVENT FOUND:", event)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print("FORM VALIDATION RESULT:", form.is_valid())
        if form.is_valid():
            registration = form.save(commit=False)
            registration.event = event
            registration.user = request.user
            registration.save()
            print("REGISTRATION SAVED SUCCESSFULLY")
            return redirect('event_list')
    else:
        form = RegistrationForm()
    return render(request, 'event_management/register_event.html', {'form': form, 'event': event})

@login_required
def registration_list(request):
    registrations = Registration.objects.filter(user=request.user)
    return render(request, 'event_management/registration_list.html', {'registrations': registrations})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse_lazy('event_list'))
    else:
        return render(request, 'event_management/login.html', {'error': 'Invalid username or password'})
    return render(request, 'event_management/login.html')
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('event_list')

def user_register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_view') 
    else:
        form = UserCreationForm()
    return render(request, 'event_management/user_register.html', {'form': form})    