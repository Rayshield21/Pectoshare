from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView
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

  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(**kwargs)
    context['profile_fields'] = self.model._meta.get_fields()
    return context