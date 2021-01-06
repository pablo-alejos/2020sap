from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView,TemplateView)

from .forms import ProjectModelForm
from .models import Project

class ProjectIndexView(ListView): 
    template_name = 'project/project_index.html'
    queryset = Project.objects.all()
############################################################
class ProjectCreateView(CreateView): 
    template_name = 'project/project_create.html'
    form_class = ProjectModelForm
    queryset = Project.objects.all() 
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            want_redirect = request.POST.get('want_redirect')
            if not want_redirect:
                self.success_url = reverse_lazy('project:project-create')
        return super(ProjectCreateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)   
############################################################
class ProjectDetailView(DetailView): 
    template_name = 'project/project_detail.html' 

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Project, id=id_)
############################################################
class ProjectUpdateView(UpdateView): 
    template_name = 'project/project_update.html'
    form_class = ProjectModelForm
    queryset = Project.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)    

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Project, id=id_)
############################################################
class ProjectDeleteView(DeleteView):
    template_name = 'project/project_delete.html'  

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Project, id=id_)

    def get_success_url(self): 
        return reverse('Project:project-index')

class ProjectJoinView(TemplateView): 
    template_name = 'project/project_join.html'
    form_class = ProjectModelForm
    queryset = Project.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)    
