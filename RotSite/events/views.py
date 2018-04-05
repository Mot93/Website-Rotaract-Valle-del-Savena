from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
# Models I creates
from .models import Events

def index(request):
    latest_event_list = Events.objects.order_by('-event_date')[:5]
    template = loader.get_template('events/index.html')
    context = {
        'latest_event_list':latest_event_list
    }
    return HttpResponse(template.render(context, request))

def detail(request, event_id):
    try:
        event = Events.objects.get(pk=event_id)
    except Events.DoesNotExist:
        raise Http404("This event does not exists")
    template = 'events/detail.html'
    context = {
        'event':event
    }
    return render (request, template, context)
    