from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models

class RegisterForm(UserCreationForm):
  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
  class Meta:
    model = models.Profile
    exclude = ('user', 'slug')

  def __init__(self,*args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['profile_pic'].widget.attrs.update({'class': 'image_input'})