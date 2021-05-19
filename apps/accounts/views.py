from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView
from . import forms, models
# Create your views here.

class Register(SuccessMessageMixin, CreateView):
  form_class = forms.RegisterForm
  success_url = reverse_lazy('accounts:login')
  success_message = 'User Registration Successful. Please Login'
  template_name = 'accounts/register.html'

class Profile(DetailView):
  model = models.Profile
  template_name = 'accounts/profile.html'

class EditProfile(UpdateView):
  model = models.Profile
  form_class = forms.ProfileForm
  template_name = 'accounts/edit_profile.html'

  def get_success_url(self):
    return reverse('accounts:profile', kwargs={'slug': self.kwargs['slug']})