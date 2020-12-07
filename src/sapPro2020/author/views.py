from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView)

from .forms import AuthorModelForm
from .models import Author

class AuthorIndexView(ListView): 
    template_name = 'author/author_index.html'
    queryset = Author.objects.all()
############################################################
class AuthorCreateView(CreateView): 
    template_name = 'author/author_create.html'
    form_class = AuthorModelForm
    queryset = Author.objects.all() 
    success_url = reverse_lazy('author:author-index')

    def form_valid(self, form):
        return super().form_valid(form)   
############################################################
class AuthorDetailView(DetailView): 
    template_name = 'author/author_detail.html' 

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Author, id=id_)
############################################################
class AuthorUpdateView(UpdateView): 
    template_name = 'author/author_update.html'
    form_class = AuthorModelForm
    queryset = Author.objects.all()
    success_url = reverse_lazy('userSap:user-index')

    def form_valid(self, form):
        return super().form_valid(form)    

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Author, id=id_)
############################################################
class AuthorDeleteView(DeleteView):
    template_name = 'author/author_delete.html'  

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Author, id=id_)

    def get_success_url(self): 
        return reverse('author:author-index')