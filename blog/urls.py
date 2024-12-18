from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('like-post/<int:post_id>/', views.like_post, name='like-post'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/create/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/change', views.PostChangeView.as_view(), name='post-change'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
    path('comment/<int:pk>/change', views.CommentChangeView.as_view(), name='comment-change'),
    path('comment/<int:pk>/delete', views.CommentDeleteView.as_view(), name='comment-delete'),
    path('profile/', views.profile, name='profile'),
    path('profile/change/', views.ChangeUserInfoView.as_view(), name='profile-change'),
    path('profile/delete/', views.DeleteUserView.as_view(), name='profile-delete'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.Register.as_view(), name='register'),
]
