from django import forms
from . import models

class PostForm(forms.ModelForm):
  class Meta:
    model = models.Post
    exclude = ['date_added']
