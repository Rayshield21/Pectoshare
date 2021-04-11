from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
User = get_user_model()
# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
  first_name = models.CharField(max_length=255, blank=True)
  last_name = models.CharField(max_length=255, blank=True)
  profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
  STATUS_CHOICES = [
    (LOOKING_FOR_WORK, 'Looking for Work'),
    (EMPLOYER, 'Employer')
  ]
  status = models.CharField(max_length=255,
    choices=STATUS_CHOICES, default=LOOKING_FOR_WORK)
  
  def __str__(self):
    if self.first_name and self.last_name:
      return "{first_name} {last_name}".format(self.first_name, self.last_name)
    return self.user

@receiver(post_save, sender=User)
def create_profile(sender, instance , created, **kwargs):
  if(created):
    Profile.objects.save(user=instance)

post_save.connect(create_profile, sender=User)