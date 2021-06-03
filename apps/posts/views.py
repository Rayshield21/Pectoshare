from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from apps.accounts.mixins import CustomLoginRequiredMixin, ObjectAccessPermissionMixin
from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from pectoshare.functions import get_conf_message
from . import models, forms

# Create your views here.

# LIST POST

class Home(generic.ListView):
  model = models.Post
  template_name = 'posts/post_all.html'
  context_object_name = 'post_list'

# LIST CATEGORIES/TOPICS

class ListCategories(generic.ListView):
  model = models.Category
  template_name = 'posts/post_categories.html'
  context_object_name = 'categories_list'

# LIST POSTS IN CATEGORY/TOPIC

class PostsInCategory(generic.DetailView):
  model = models.Category
  template_name = 'posts/post_in_category.html'


# SEARCH 

class SearchTitle(generic.ListView):
  model = models.Post
  template_name = 'posts/post_results.html'

  def get_queryset(self):
    query = self.request.GET.get('query')
    post_list = models.Post.objects.filter(
      Q(title__icontains=query)
    )
    return post_list

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['search'] = self.request.GET.get('query')
    return context

# POST DETAIL 

class SinglePost(generic.DetailView):
  model = models.Post
  template_name = 'posts/post_detail.html'

  def get_context_data(self, **kwargs):
    instance = self.get_object()
    context = super().get_context_data(**kwargs)
    related = models.Post.objects.filter(
      Q(title__contains=instance.title),
      ~Q(id__contains=instance.id)
    )
    if instance.category:
      related = models.Post.objects.filter(
        Q(title__contains=instance.title) | 
        Q(category__name__contains=instance.category.name),
        ~Q(id__contains=instance.id)
      )
    
    context['related_posts'] = related
    return context

# CREATE POST 

class CreatePost(CustomLoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
  model = models.Post
  template_name = 'posts/post_form.html'
  form_class = forms.PostForm
  success_message = get_conf_message('SUCCESS', 'POST_ADD')

  class Meta:
    ordering = ['-date_modified', '-date_added']

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.user = self.request.user
    self.object.save()
    return super().form_valid(form)

# UPDATE POST 

class UpdatePost(ObjectAccessPermissionMixin, SuccessMessageMixin,generic.UpdateView):
  model = models.Post
  form_class = forms.PostForm
  template_name = 'posts/post_form.html'
  success_message = get_conf_message('SUCCESS', 'POST_UPDATE')

  def handle_no_permission(self):
    return HttpResponseRedirect(reverse('posts:single', 
      kwargs={'pk': self.kwargs['pk']}))

  def get_success_url(self):
    return reverse('posts:single', kwargs={'pk': self.kwargs['pk']})


# DELETE POST 

class DeletePost(ObjectAccessPermissionMixin, SuccessMessageMixin, generic.DeleteView):
  model = models.Post
  success_url = reverse_lazy('home')
  success_message = get_conf_message('SUCCESS', 'POST_DELETE')

  @method_decorator(require_POST)
  def get(self, request, *args, **kwargs):
    """
      Fires HTTP405 if the url for confirm delete view is manually typed and visited.
      Confirmation Delete is working in the front end via modal.
    """
    pass
  
  def handle_no_permission(self):
    return HttpResponseRedirect(reverse('posts:single', 
      kwargs={'pk': self.kwargs['pk']}))

# LIKE POST 

class LikePost(CustomLoginRequiredMixin, generic.RedirectView):

  def get_redirect_url(self, *args, **kwargs):
    return reverse('home')

  def get(self, request, *args, **kwargs):
    post_instance = models.Post.objects.get(id=self.kwargs.get('pk'))
    like, created = models.Like.objects.get_or_create(is_liked=True, user=request.user, post=post_instance)

    if created:
      like.save()
      messages.add_message(self.request, messages.SUCCESS, 
        get_conf_message('SUCCESS', 'LIKE'))
    else:
      like.delete()
      messages.add_message(self.request, messages.SUCCESS,
        get_conf_message('SUCCESS', 'UNLIKE'))
    return super().get(request, *args, **kwargs)