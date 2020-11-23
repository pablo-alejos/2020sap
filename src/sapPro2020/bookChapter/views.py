from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy

from django.views.generic import (
    CreateView, DetailView, ListView, UpdateView, DeleteView)

from .forms import BookChapterModelForm
from .models import BookChapter


class BookChapterIndexView(ListView):
    template_name = 'bookChapter/bookChapter_index.html'
    queryset = BookChapter.objects.all()
############################################################


class BookChapterCreateView(CreateView):
    template_name = 'bookChapter/bookChapter_create.html'
    form_class = BookChapterModelForm
    queryset = BookChapter.objects.all()

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            want_redirect = request.POST.get('want_redirect')
            if not want_redirect:
                self.success_url = reverse_lazy(
                    'bookChapter:bookChapter-create')
        return super(BookChapterCreateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
############################################################


class BookChapterDetailView(DetailView):
    template_name = 'bookChapter/bookChapter_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(BookChapter, id=id_)
############################################################


class BookChapterUpdateView(UpdateView):
    template_name = 'bookChapter/bookChapter_update.html'
    form_class = BookChapterModelForm
    queryset = BookChapter.objects.all()

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            want_redirect = request.POST.get('want_redirect')
            if not want_redirect:
                self.success_url = reverse_lazy(
                    'bookChapter:bookChapter-update', kwargs={'id': self.kwargs.get("id")})
        return super(BookChapterUpdateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(BookChapter, id=id_)
############################################################


class BookChapterDeleteView(DeleteView):
    template_name = 'bookChapter/bookChapter_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(BookChapter, id=id_)

    def get_success_url(self):
        return reverse('bookChapter:bookChapter-index')