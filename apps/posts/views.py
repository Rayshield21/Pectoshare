from django.shortcuts import render
from . import models
from django.views import generic
# Create your views here.

# List Post
class Home(generic.ListView):
  model = models.Post
  template_name = 'posts/post_all.html'
  context_object_name = 'post_list'


class SinglePost(generic.DetailView):
  model = models.Post
  template_name = 'posts/post_detail.html'

class CreatePost(generic.CreateView):
  model = models.Post
  template_name = 'posts/post_form.html'
  fields = ['title', 'image']

class UpdatePost(generic.UpdateView):
  pass

class DeletePost(generic.DeleteView):
  pass

