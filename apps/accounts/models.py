from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
  class WorkStatus(models.TextChoices):
    LOOKING_FOR_WORK = 'Looking for Work', _('Looking for Work')
    EMPLOYER = 'Employer', _('Employer')
  user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
  name = models.CharField(max_length=255, blank=True)
  profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
  status = models.CharField(max_length=255,
    choices=WorkStatus.choices, blank=True)
  location = models.CharField(max_length=255, blank=True)
  company = models.CharField(max_length=255, blank=True)
  website = models.CharField(max_length=255, blank=True)
  bio = models.TextField(blank=True)
  slug = models.SlugField(allow_unicode=True, unique=True)
  
  def __str__(self):
    if self.name:
      return "{name}".format(self.name)
    return self.user.username

  def save(self, *args, **kwargs):
    self.slug = slugify(self.user.username)
    super().save(*args, **kwargs)

@receiver(post_save, sender=User)
def create_profile(sender, instance , created, **kwargs):
  if created:
    Profile.objects.create(user=instance)
    instance.profile.save()