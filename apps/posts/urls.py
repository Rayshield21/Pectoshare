from . import views
from django.urls import path


app_name = 'posts'
urlpatterns = [
  path('create/', views.CreatePost.as_view(), name='create'),
  path('photo/<int:pk>', views.SinglePost.as_view(), name='single'),
  path('delete/<int:pk>', views.DeletePost.as_view(), name='delete'),
  path('update/<int:pk>', views.UpdatePost.as_view(), name='update')
]
