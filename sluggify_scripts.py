"""
  This script for sluggifying all data that already existed prior to adding a slugfield.
"""
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pectoshare.settings')

import django

django.setup()

from apps.posts.models import Category
from django.utils.text import slugify

def sluggify_existing_fields(model):
  objects = model.objects.all()

  for obj in objects:
    obj.slug = slugify(str(obj))
    obj.save()
    
if __name__ == '__main__':
  print('Sluggifying Existing Fields')
  sluggify_existing_fields(Category)
  print("Sluggify Success!")