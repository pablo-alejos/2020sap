from django.shortcuts import render
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView)
from .forms import ForumModelForm
from .forms import SymposiumModelForm
from .forms import CongressModelForm
from .models import Forum,Symposium,Congress
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy

# Create your views here.

class EventIndexView(ListView): 
    template_name = 'event/event_index.html'
    queryset = Forum.objects.all()
    queryset = Congress.objects.all()
    queryset = Symposium.objects.all()
    paginate_by=1
################################################
class ForumIndexView(ListView): 
    template_name = 'forum/forum_index.html'
    queryset = Forum.objects.all()
    paginate_by=1
################################################ 
class ForumCreateView(CreateView): 
    template_name = 'forum/forum_create.html'
    form_class = ForumModelForm
    queryset = Forum.objects.all()
    success_url = reverse_lazy('event:forum-index')
    def form_valid(self, form):
        return super().form_valid(form)
############################################################
class ForumDetailView(DetailView): 
    template_name = 'forum/forum_detail.html' 

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Forum, id=id_)
############################################################
class ForumUpdateView(UpdateView): 
    template_name = 'forum/forum_update.html'
    form_class = ForumModelForm
    queryset = Forum.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)    

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Forum, id=id_)
############################################################
class ForumDeleteView(DeleteView): 
    template_name = 'forum/forum_delete.html'  

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Forum, id=id_)

    def get_success_url(self): 
        return reverse('userSayac:academy-index')


class SymposiumIndexView(ListView): 
    template_name = 'symposium/symposium_index.html'
    queryset = Symposium.objects.all()
    paginate_by=1
############################################################
class SymposiumCreateView(CreateView): 
    template_name = 'symposium/symposium_create.html'
    form_class = SymposiumModelForm
    queryset = Symposium.objects.all() 
    success_url = reverse_lazy('event:symposium-index')
    def form_valid(self, form):
        return super().form_valid(form)   
############################################################
class SymposiumDetailView(DetailView): 
    template_name = 'symposium/symposium_detail.html' 

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Symposium, id=id_)
############################################################
class SymposiumUpdateView(UpdateView): 
    template_name = 'symposium/symposium_update.html'
    form_class = SymposiumModelForm
    queryset = Symposium.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)    

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Symposium, id=id_)
############################################################
class SymposiumDeleteView(DeleteView):  
    template_name = 'symposium/symposium_delete.html'  

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Symposium, id=id_)

    def get_success_url(self): 
        return reverse('userSayac:symposium-index')


class CongressIndexView(ListView): 
    template_name = 'congress/congress_index.html'
    queryset = Congress.objects.all()
    paginate_by=1


############################################################
class CongressCreateView(CreateView): 
    template_name = 'congress/congress_create.html'
    form_class = CongressModelForm
    queryset = Congress.objects.all() 
    success_url = reverse_lazy('event:congress-index')
    
    def form_valid(self, form):
        return super().form_valid(form)   
############################################################
class CongressDetailView(DetailView): 
    template_name = 'congress/congress_detail.html' 

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Congress, id=id_)
############################################################
class CongressUpdateView(UpdateView): 
    template_name = 'congress/congress_update.html'
    form_class = CongressModelForm
    queryset = Congress.objects.all()
    success_url = reverse_lazy('userSap:user-index')

    def form_valid(self, form):
        return super().form_valid(form)    

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Congress, id=id_)
############################################################
class CongressDeleteView(DeleteView):
    template_name = 'congress/congress_delete.html'  

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Congress, id=id_)

    def get_success_url(self): 
        return reverse('congress:congress-index')