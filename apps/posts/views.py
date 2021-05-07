from django.shortcuts import render
from apps.accounts.mixins import CustomLoginRequiredMixin
from . import models
from django.views import generic
from django.contrib import messages
# Create your views here.

# List Post
class Home(generic.ListView):
  model = models.Post
  template_name = 'posts/post_all.html'
  context_object_name = 'post_list'


class SinglePost(generic.DetailView):
  model = models.Post
  template_name = 'posts/post_detail.html'

class CreatePost(CustomLoginRequiredMixin, generic.CreateView):
  model = models.Post
  template_name = 'posts/post_form.html'
  fields = ['title', 'image']

class UpdatePost(generic.UpdateView):
  pass

class DeletePost(generic.DeleteView):
  pass

