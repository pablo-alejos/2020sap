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
from django.views.generic import (CreateView, DetailView, ListView, UpdateView,
                                  DeleteView, TemplateView)
from itertools import chain
# , PasswordChangeForm
from .forms import UserSapModelForm, UserSapCreationForm, UserSapChangeForm, LoginForm
from .models import UserSap
from book.models import Book
from article.models import Article
from bookChapter.models import BookChapter
from project.models import Project

from .forms import AcademyModelForm
from .forms import ProgramModelForm
from .forms import AccountModelForm
from .models import Academy, Program, Account


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
        context['project_list'] = Project.objects.all()
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


########################################


class PublicationUserView(TemplateView):
    template_name = "user/user_product_panel.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_list = Book.objects.filter(user=self.request.user)
        bookChapter_list = BookChapter.objects.filter(user=self.request.user)
        article_list = Article.objects.filter(user=self.request.user)
        product_list = list(chain(article_list, book_list, bookChapter_list))
        context['book_list'] = book_list
        context['bookChapter_list'] = bookChapter_list
        context['article_list'] = article_list
        context['product_list'] = product_list
        return context


class AcademyIndexView(ListView):
    template_name = 'academy/academy_index.html'
    queryset = Academy.objects.all()


################################################
class AcademyCreateView(CreateView):
    template_name = 'academy/academy_create.html'
    form_class = AcademyModelForm
    queryset = Academy.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)


############################################################
class AcademyDetailView(DetailView):
    template_name = 'academy/academy_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Academy, id=id_)


############################################################
class AcademyUpdateView(UpdateView):
    template_name = 'academy/academy_update.html'
    form_class = AcademyModelForm
    queryset = Academy.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Academy, id=id_)


############################################################
class AcademyDeleteView(DeleteView):
    template_name = 'academy/academy_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Academy, id=id_)

    def get_success_url(self):
        return reverse('userSayac:academy-index')


class ProgramIndexView(ListView):
    template_name = 'program/program_index.html'
    queryset = Program.objects.all()


############################################################
class ProgramCreateView(CreateView):
    template_name = 'program/program_create.html'
    form_class = ProgramModelForm  #falta validar el registro de los datos
    queryset = Program.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)


############################################################
class ProgramDetailView(DetailView):
    template_name = 'program/program_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Program, id=id_)


############################################################
class ProgramUpdateView(UpdateView):
    template_name = 'program/program_update.html'
    form_class = ProgramModelForm
    queryset = Program.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Program, id=id_)


############################################################
class ProgramDeleteView(DeleteView):
    template_name = 'program/program_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Program, id=id_)

    def get_success_url(self):
        return reverse('userSayac:program-index')


class AccountIndexView(ListView):
    template_name = 'account/account.html'
    queryset = Account.objects.all()


############################################################
class AccountCompleteView(UpdateView):
    template_name = 'account/account_complete.html'
    form_class = AccountModelForm
    queryset = Account.objects.all()
    success_url = reverse_lazy('userSap:user-index')

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Account, id=id_)


############################################################
class AccountDetailView(DetailView):
    template_name = 'account/account_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Account, id=id_)


############################################################
class AccountUpdateView(UpdateView):
    template_name = 'account/account_update.html'
    form_class = AccountModelForm
    queryset = Account.objects.all()
    success_url = reverse_lazy('userSap:user-index')

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Account, id=id_)


############################################################
class AccountDeleteView(DeleteView):
    template_name = 'account/account_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Account, id=id_)

    def get_success_url(self):
        return reverse('userSap:account-index')
