from django.urls import path, include
from . import views


urlpatterns = [
    path('creators', views.creators, name='creators'),
    path('<int:post_id>/', views.detailedpost, name='detailedpost'),
    path('createpost', views.createpost, name='createpost'),
    path('upvotepost/<int:post_id>', views.upvotepost, name='upvotepost'),
    path('create_comment/<int:post_id>', views.postcomment, name='postcomment'),
    path('upvotecomment/<int:post_id>/<int:comment_id>', views.upvotecomment, name='upvotecomment'),
]
