from django.shortcuts import render
from django.conf import settings
from apps.accounts.mixins import CustomLoginRequiredMixin
from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
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

class CreatePost(CustomLoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
  model = models.Post
  template_name = 'posts/post_form.html'
  form_class = forms.PostForm
  success_message = settings.MESSAGES['SUCCESS']['POST_ADD']

  class Meta:
    ordering = ['-date_modified', '-date_added']

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.author = self.request.user
    self.object.save()
    return super().form_valid(form)

class UpdatePost(SuccessMessageMixin,generic.UpdateView):
  model = models.Post
  form_class = forms.PostForm
  template_name = 'posts/post_form.html'
  success_message = settings.MESSAGES['SUCCESS']['POST_UPDATE']
  
  def get_success_url(self):
    return reverse('posts:single', kwargs={'pk': self.kwargs['pk']})

class DeletePost(SuccessMessageMixin, generic.DeleteView):
  model = models.Post
  success_url = reverse_lazy('home')
  success_message = settings.MESSAGES['SUCCESS']['POST_DELETE']

  @method_decorator(require_POST)
  def get(self, request, *args, **kwargs):
    """
      Fires HTTP405 if the url for confirm delete view is manually typed and visited.
      Confirmation Delete is working in the front end via modal.
    """
    pass

class LikePost(CustomLoginRequiredMixin, generic.RedirectView):

  def get_redirect_url(self, *args, **kwargs):
    return reverse('home')

  def get(self, request, *args, **kwargs):
    post_instance = models.Post.objects.get(id=self.kwargs.get('pk'))
    like, created = models.Like.objects.get_or_create(is_liked=True, user=request.user, post=post_instance)

    if created:
      like.save()
      messages.add_message(self.request, messages.SUCCESS, settings.MESSAGES["SUCCESS"]["LIKE"])
    else:
      like.delete()
      messages.add_message(self.request, messages.SUCCESS, settings.MESSAGES["SUCCESS"]["UNLIKE"])
    return super().get(request, *args, **kwargs)