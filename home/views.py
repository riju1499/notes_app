from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.shortcuts import redirect
from django.contrib.auth import logout

# Create your views here.
class SignupView(CreateView):
    form_class=UserCreationForm
    template_name='home/register.html'
    # success_url='smart/notes'
    success_url = reverse_lazy('notes.list')

    def get(self,request,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request,*args,**kwargs)

class LoginInterfaceView(LoginView):
    template_name='home/login.html'

# class LogoutInterfaceView(LogoutView):
#     template_name='home/logout.html'
def logout_view(request):
    logout(request)
    # Redirect to a specific URL after logout
    return redirect('home')
   

class HomeView(TemplateView):
    template_name='home/welcome.html'

 

