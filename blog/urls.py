from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/add/', views.PostCreateView.as_view(), name='post_add'),
]
