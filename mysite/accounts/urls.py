from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/',views.signup,name='signup'),
    path('profile/<int:pk>/', views.profile_view, name='profile'),
    path('profile/update/<int:pk>/', views.profile_update, name='profile-update'),
    
    
    
]

htmx_patterns=[
    path('profile/<int:pk>/add-follow/', views.follow,name='follow-profile'),
]
urlpatterns+=htmx_patterns