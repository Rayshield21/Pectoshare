from . import views
from django.urls import path


app_name = 'posts'
urlpatterns = [
  path('create/', views.CreatePost.as_view(), name='create'),
  path('photo/<int:pk>', views.SinglePost.as_view(), name='single'),
]
