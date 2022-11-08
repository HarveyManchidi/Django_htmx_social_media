from django.urls import path
from socialnetwork import views
#from accounts import views as accounts_views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('posts/<int:pk>/', views.post_detail, name='post-detail'),
    path('create_post/', views.post_create, name='post-create'),
    path('update_post/<int:pk>/', views.post_update, name='post-update'),
    path('delete_post/<int:pk>/', views.post_delete, name='post-delete'),
    path('like_post/<int:pk>/', views.like_post, name='like-post'),
]
htmx_patterns = [
    path('posts/<int:pk>/add-comment/', views.comments, name='add-comment'),
    path('home/posts/<int:post_pk>/<int:pk>/follow/', views.feed_follow, name='feed-follow'),
    path('posts/<int:post_pk>/profile/<int:pk>/follow/',
         views.detail_follow, name='detail-follow'),



]
urlpatterns += htmx_patterns
