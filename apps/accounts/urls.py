from . import views
from django.urls import path

app_name = 'accounts'
urlpatterns = [
  path('login/', views.Login.as_view(), name='login'),
  path('logout', views.logout_view, name='logout'),
  path('register/', views.Register.as_view(), name='register'),
  path('profile/<slug>', views.Profile.as_view(), name='profile'),
  path('profile/edit/<slug>/<int:pk>', views.EditProfile.as_view(), name='edit_profile'),
]
