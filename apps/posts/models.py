from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=255, blank=False)
  cover_image = models.ImageField(upload_to='cover_images/', blank=True, null=True)
  description = models.TextField()
  slug = models.SlugField(allow_unicode=True, unique=True, null=True)
  
  def __str__(self):
    return self.name
    
class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post', default=None)
  title = models.CharField(max_length=255, default=None)
  image = models.ImageField(upload_to='images/')
  date_added = models.DateTimeField(editable=False)
  date_modified = models.DateTimeField(editable=False, blank=True, null=True)
  category = models.ForeignKey(Category, related_name='category_posts', on_delete=models.CASCADE, null=True, blank=True)

  class Meta:
    ordering = ['-date_modified', '-date_added']

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse("home")
  
  def save(self, *args, **kwargs):
    if not self.id:
      self.date_added = timezone.now()
    else:
      self.date_modified = timezone.now()
    return super(Post, self).save(*args, **kwargs)

class Like(models.Model):
  is_liked = models.BooleanField()
  user = models.ForeignKey(User, related_name='user_likes', on_delete=models.CASCADE)
  post = models.ForeignKey(Post, related_name='post_likes', on_delete=models.CASCADE)
  
  def __str__(self):
    return '{}'.format(self.is_liked)