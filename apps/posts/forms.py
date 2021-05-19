from django import forms
from . import models

class PostForm(forms.ModelForm):
  class Meta:
    model = models.Post
    exclude = ['date_added', 'date_modified', 'author']

  def __init__(self,*args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['image'].widget.attrs.update({'class': 'image_input'})