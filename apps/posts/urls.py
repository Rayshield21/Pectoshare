from . import views
from django.urls import path

app_name = 'posts'
urlpatterns = [
  path('create/', views.CreatePost.as_view(), name='create'),
  path('view/topics/', views.ListCategories.as_view(), name='topics'),
  path('view/topic/<slug>', views.PostsInCategory.as_view(), name='topic_posts'),
  path('photo/<int:pk>', views.SinglePost.as_view(), name='single'),
  path('delete/<int:pk>', views.DeletePost.as_view(), name='delete'),
  path('update/<int:pk>', views.UpdatePost.as_view(), name='update'),
  path('like/<int:pk>', views.LikePost.as_view(), name='like'),
  path('search/', views.SearchTitle.as_view(), name='search_title'),
  # path('like/<int:pk>', views.Like, name='like')
]
