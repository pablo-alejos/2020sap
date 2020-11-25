from django.shortcuts import render
from django.views.generic import (
    CreateView, DetailView, ListView, UpdateView, DeleteView)
from .forms import EventModelForm
from .models import Event
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy


# Create your views here.


class EventUpdateView(UpdateView):
    template_name = 'event/event_update.html'
    form_class = EventModelForm
    success_url = reverse_lazy('event:event-index')
    queryset = Event.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Event, id=id_)
############################################################


class EventDeleteView(DeleteView):
    template_name = 'event/event_delete.html'
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Event, id=id_)

    def get_success_url(self):
        return reverse('event:event-index')

############################################################


class EventIndexView(ListView):
    template_name = 'event/event_index.html'
    queryset = Event.objects.order_by('eventCreated')
    context_object_name = 'event_list'
    paginate_by = 25
################################################


class EventCreateView(CreateView):
    template_name = 'event/event_create.html'
    form_class = EventModelForm
    queryset = Event.objects.all()
    success_url = reverse_lazy('event:event-index')

    def form_valid(self, form):
        return super().form_valid(form)
################################################
