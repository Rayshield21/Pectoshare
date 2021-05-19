from django.shortcuts import render
from apps.accounts.mixins import CustomLoginRequiredMixin
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from . import models, forms
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
  form_class = forms.PostForm

  class Meta:
    ordering = ['-date_modified', '-date_added']

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.author = self.request.user
    self.object.save()
    return super().form_valid(form)


class UpdatePost(generic.UpdateView):
  model = models.Post
  form_class = forms.PostForm
  template_name = 'posts/post_form.html'
  
  def get_success_url(self):
    return reverse('posts:single', kwargs={'pk': self.kwargs['pk']})

class DeletePost(generic.DeleteView):
  model = models.Post
  success_url = reverse_lazy('home')


  @method_decorator(require_POST)
  def get(self, request, *args, **kwargs):
    """
      Fires HTTP405 if the url for confirm delete view is manually typed and visited.
      Confirmation Delete is working in the front end via modal.
    """
    pass