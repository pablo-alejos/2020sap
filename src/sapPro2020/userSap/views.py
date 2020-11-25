from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.http import HttpResponseRedirect
from django.views.generic import (
    CreateView, DetailView, ListView, UpdateView, DeleteView)
from itertools import chain
# , PasswordChangeForm
from .forms import UserSapModelForm, UserSapCreationForm, UserSapChangeForm, LoginForm
from .models import UserSap
from book.models import Book
from article.models import Article
from bookChapter.models import BookChapter


class UserIndexView(DetailView):
    template_name = 'user/user_index.html'
    queryset = UserSap.objects.all()

    def get_object(self):
        id_ = self.request.user.id
        return get_object_or_404(UserSap, id=id_)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.filter(user=self.request.user.id)
        context['bookChapter_list'] = BookChapter.objects.filter(
            user=self.request.user.id)
        context['article_list'] = Article.objects.filter(
            user=self.request.user.id)
        article_list = Article.objects.filter(user=self.request.user.id)
        book_list = Book.objects.filter(user=self.request.user.id)
        chapter_list = BookChapter.objects.filter(user=self.request.user.id)
        product_list = list(chain(article_list, book_list, chapter_list))
        context['product_list'] = product_list
        return context

############################################################


class UserCreateView(CreateView):
    template_name = 'user/user_create.html'
    form_class = UserSapCreationForm
    queryset = UserSap.objects.all()
    success_url = reverse_lazy('userSap:user-login')

    def form_valid(self, form):
        return super().form_valid(form)
############################################################


class UserDetailView(DetailView):
    template_name = 'user/user_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(UserSap, id=id_)
############################################################


class UserUpdateView(UpdateView):
    template_name = 'user/user_update.html'
    form_class = UserSapChangeForm
    queryset = UserSap.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(UserSap, id=id_)
############################################################


class UserChangePasswordView(PasswordChangeView):
    template_name = 'user/user_update_password.html'
    #form_class = PasswordChangeForm
    queryset = UserSap.objects.all()
    success_url = reverse_lazy('userSap:user-index')

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(UserSap, id=id_)
############################################################


class UserDeleteView(DeleteView):
    template_name = 'user/user_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(UserSap, id=id_)

    def get_success_url(self):
        return reverse('userSap:user-index')


class UserSapLoginView(LoginView):
    template_name = 'user/user_login.html'
    authentication_form = LoginForm

    """
    success_url = reverse_lazy('userSap:user-index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(UserSapLoginView,self).dispatch(request,*args,**kwargs)

    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(UserSapLoginView,self).form_valid(form)
"""


def UserSapLogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('userSap:user-login'))
