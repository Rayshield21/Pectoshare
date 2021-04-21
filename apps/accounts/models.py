from django.db import models
from django.contrib.auth import models as auth_models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(auth_models.User, auth_models.PermissionsMixin):
  def __str__(self):
    return self.username
    
# Create your models here.
class Profile(models.Model):
  class WorkStatus(models.TextChoices):
    LOOKING_FOR_WORK = 'Looking for Work', _('Looking for Work')
    EMPLOYER = 'Employer', _('Employer')
  user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
  first_name = models.CharField(max_length=255, blank=True)
  last_name = models.CharField(max_length=255, blank=True)
  profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

  status = models.CharField(max_length=255,
    choices=WorkStatus.choices, default=WorkStatus.LOOKING_FOR_WORK, blank=True)
  
  def __str__(self):
    if self.first_name and self.last_name:
      return "{first_name} {last_name}".format(self.first_name, self.last_name)
    return self.user

@receiver(post_save, sender=User)
def create_profile(sender, instance , created, **kwargs):
  if(created):
    Profile.objects.save(user=instance)

post_save.connect(create_profile, sender=User)