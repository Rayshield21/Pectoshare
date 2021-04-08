from django.db import models
from django.shortcuts import reverse
# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length=100, unique=True)
  image = models.ImageField(upload_to='images/')
  date_added = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return self.title

  def get_absolute_url(self):
      return reverse("home")
  
  