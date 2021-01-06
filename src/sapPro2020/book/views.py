from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy

from itertools import chain

from django.views.generic import (CreateView, DetailView, ListView, UpdateView,
                                  DeleteView)

from .forms import BookModelForm
from userSap.models import Academy, Program
from event.models import Event
from tag.models import Tag
from .models import Book


class BookIndexView(ListView):
    template_name = 'book/book_index.html'
    queryset = Book.objects.all()


############################################################


class BookCreateView(CreateView):
    template_name = 'book/book_create.html'
    form_class = BookModelForm
    queryset = Book.objects.all()

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            want_redirect = request.POST.get('want_redirect')
            if not want_redirect:
                self.success_url = reverse_lazy('book:book-create')
        return super(BookCreateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['program_list'] = Program.objects.order_by('name')
        context['academy_list'] = Academy.objects.order_by('name')
        context['event_list'] = Event.objects.order_by('name')
        return context

    def form_valid(self, form):
        #form.instance.user = self.request.user
        return super().form_valid(form)


############################################################


class BookDetailView(DetailView):
    template_name = 'book/book_detail.html'
    queryset = Book.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Book, id=id_)


############################################################


class BookUpdateView(UpdateView):
    template_name = 'book/book_update.html'
    form_class = BookModelForm
    queryset = Book.objects.all()

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            want_redirect = request.POST.get('want_redirect')
            if not want_redirect:
                self.success_url = reverse_lazy(
                    'book:book-update', kwargs={'id': self.kwargs.get("id")})
        return super(BookUpdateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['program_list'] = Program.objects.order_by('name')
        context['academy_list'] = Academy.objects.order_by('name')
        context['event_list'] = Event.objects.order_by('name')
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Book, id=id_)


############################################################


class BookDeleteView(DeleteView):
    template_name = 'book/book_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Book, id=id_)

    def get_success_url(self):
        return reverse('userSap:user-product-panel')
