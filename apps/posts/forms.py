from unicodedata import category
from django import forms
from . import models

class PostForm(forms.ModelForm):
  category = forms.ModelChoiceField(queryset=models.Category.objects.all(), to_field_name='name', required=False)
  class Meta:
    model = models.Post
    exclude = ['date_added', 'date_modified', 'user']

  def __init__(self,*args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['image'].widget.attrs.update({'class': 'image_input'})