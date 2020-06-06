from django.urls import path, include
from . import views


urlpatterns = [
    path('creators', views.creators, name='creators'),
    path('<int:post_id>/', views.detailedpost, name='detailedpost'),
    path('createpost', views.createpost, name='createpost'),
    path('<int:post_id>/upvotepost', views.upvotepost, name='upvotepost'),
    path('create_comment/<int:post_id>', views.postcomment, name='postcomment'),
]
