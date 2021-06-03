from django.http.response import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import logout, views
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView
from apps.accounts.mixins import ObjectAccessPermissionMixin
from pectoshare.functions import get_conf_message
from . import forms, models
# Create your views here.

def logout_view(request):
  logout(request)
  messages.add_message(request, messages.SUCCESS, 
    get_conf_message('SUCCESS', 'LOGOUT'))
  return HttpResponseRedirect(reverse('home'))

class Login(SuccessMessageMixin, views.LoginView):
  template_name = 'accounts/login.html'
  success_message = get_conf_message('SUCCESS', 'LOGIN')

class Register(SuccessMessageMixin, CreateView):
  form_class = forms.RegisterForm
  success_url = reverse_lazy('accounts:login')
  success_message = get_conf_message('SUCCESS', 'REGISTER')
  template_name = 'accounts/register.html'

class Profile(DetailView):
  model = models.Profile
  template_name = 'accounts/profile.html'

class EditProfile(ObjectAccessPermissionMixin, SuccessMessageMixin, UpdateView):
  model = models.Profile
  form_class = forms.ProfileForm
  template_name = 'accounts/edit_profile.html'
  success_message = get_conf_message('SUCCESS', 'PROFILE_UPDATE')

  def handle_no_permission(self):
    return HttpResponseRedirect(reverse('accounts:profile', 
      kwargs={'slug': self.kwargs['slug']}))

  def get_success_url(self):
    return reverse('accounts:profile', kwargs={'slug': self.kwargs['slug']})