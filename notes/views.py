from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Notes
from django.views.generic import CreateView, ListView,DetailView,UpdateView,DeleteView
from .forms import Notesform
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.db.models import Q

# Create your views here.
class NotesDeleteView(LoginRequiredMixin,DeleteView):
    model=Notes
    success_url='/smart/notes'
    template_name='notes/notes_delete.html'
    login_url= "/login"
    def get_queryset(self):
        return self.request.user.notes.all()


class NotesUpdateView(LoginRequiredMixin,UpdateView):
    model=Notes
    success_url='/smart/notes'
    form_class=Notesform
    login_url= "/login"
    def get_queryset(self):
        return self.request.user.notes.all()
    
class NotesCreateView(CreateView):
    model=Notes
    success_url='/smart/notes'
    form_class=Notesform
    login_url= "/login"
    def form_valid(self,form):
        self.object=form.save(commit=False)
        self.object.user=self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    
class NotesListView(LoginRequiredMixin,ListView):
    model= Notes
    context_object_name="notes"
    login_url= "/login"
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['notes'] = context['notes'].filter(user=self.request.user)
        # context['count'] = context ['notes'].filter(complete=False).count()

        search_input= self.request.GET.get('search-area') or ''
        if search_input:
            context['notes']= context['notes'].filter(title__icontains=search_input)
            context['search_input'] = search_input
        return context    



class NotesDetailView(LoginRequiredMixin,DetailView):
    model=Notes
    context_object_name="note"
    login_url= "/login"
    def get_queryset(self):
        return self.request.user.notes.all()

