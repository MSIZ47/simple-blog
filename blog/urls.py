from django.contrib import admin
from django.urls import path, include
from blog.views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>/', PostDetail.as_view(), name ='post_detail'),
    path('create_post/', PostCreate.as_view(), name='create_post'),
    path('<int:pk>/update', PostUpdate.as_view(), name='update_post'),
    path('<int:pk>/delete', PostDelete.as_view(), name='delete_post'),
]
