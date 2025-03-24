from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event

def event_list(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

@login_required
def event_create(request):
    if request.method == 'POST':
        # Add form handling logic here
        pass
    return render(request, 'events/event_form.html')