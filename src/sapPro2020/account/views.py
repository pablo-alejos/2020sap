from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView)

from .forms import AcademyModelForm
from .forms import ProgramModelForm
from .forms import AccountModelForm
from .models import Academy,Program,Account

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
    form_class = ProgramModelForm #falta validar el registro de los datos
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
class AccountCreateView(CreateView): 
    template_name = 'account/account_create.html'
    form_class = AccountModelForm
    queryset = Account.objects.all() 
    success_url = reverse_lazy('userSap:user-index')

    def form_valid(self, form):
        return super().form_valid(form)   
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
        return reverse('account:account-index')
