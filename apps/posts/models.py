from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils import timezone
# Create your models here.

class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post', default=None)
  title = models.CharField(max_length=255, default=None)
  image = models.ImageField(upload_to='images/')
  date_added = models.DateTimeField(editable=False)
  date_modified = models.DateTimeField(editable=False, blank=True, null=True)

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