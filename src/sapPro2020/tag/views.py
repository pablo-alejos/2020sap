from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy

from django.views.generic import (
    CreateView, DetailView, ListView, UpdateView, DeleteView)

from .models import Tag
from .forms import TagModelForm


class TagIndexView(ListView):
    template_name = 'tag/tag_index.html'
    queryset = Tag.objects.all()
############################################################


class TagCreateView(CreateView):
    template_name = 'tag/tag_create.html'
    form_class = TagModelForm
    queryset = Tag.objects.all()
    success_url = reverse_lazy('tag:tag-index')

    def form_valid(self, form):
        return super().form_valid(form)
############################################################


class TagDetailView(DetailView):
    template_name = 'tag/tag_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Tag, id=id_)
############################################################


class TagUpdateView(UpdateView):
    template_name = 'tag/tag_update.html'
    form_class = TagModelForm
    queryset = Tag.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Tag, id=id_)
############################################################


class TagDeleteView(DeleteView):
    template_name = 'tag/tag_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Tag, id=id_)

    def get_success_url(self):
        return reverse('tag:tag-index')