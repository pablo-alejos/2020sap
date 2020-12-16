from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy

from django.views.generic import (
    CreateView, DetailView, ListView, UpdateView, DeleteView)

from .forms import ArticleModelForm, JournalModelForm
from .models import Article
from .models import Journal


class ArticleIndexView(ListView):
    template_name = 'article/article_index.html'
    queryset = Article.objects.all()
############################################################


class ArticleCreateView(CreateView):
    template_name = 'article/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_journal'] = JournalModelForm
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            want_redirect = request.POST.get('want_redirect')
            if not want_redirect:
                self.success_url = reverse_lazy('article:article-create')
        return super(ArticleCreateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        #form.instance.user = self.request.user
        return super().form_valid(form)
############################################################


class ArticleDetailView(DetailView):
    template_name = 'article/article_detail.html'
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)
############################################################


class ArticleUpdateView(UpdateView):
    template_name = 'article/article_update.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            want_redirect = request.POST.get('want_redirect')
            if not want_redirect:
                self.success_url = reverse_lazy(
                    'article:article-update', kwargs={'id': self.kwargs.get("id")})
        return super(ArticleUpdateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)
############################################################


class ArticleDeleteView(DeleteView):
    template_name = 'article/article_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('article:article-index')


class JournalIndexView(ListView):
    template_name = 'journal/journal_index.html'
    queryset = Journal.objects.all()
############################################################


class JournalCreateView(CreateView):
    template_name = 'journal/journal_create.html'
    form_class = JournalModelForm
    queryset = Journal.objects.all()

    def form_valid(self, form):
        print("form validated")
        return super().form_valid(form)
############################################################


class JournalDetailView(DetailView):
    template_name = 'journal/journal_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Journal, id=id_)
############################################################


class JournalUpdateView(UpdateView):
    template_name = 'journal/journal_update.html'
    form_class = JournalModelForm
    queryset = Journal.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Journal, id=id_)
############################################################


class JournalDeleteView(DeleteView):
    template_name = 'journal/journal_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Journal, id=id_)

    def get_success_url(self):
        return reverse('article:journal-index')

