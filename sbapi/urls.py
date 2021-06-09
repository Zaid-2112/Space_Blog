from django.urls import path
from .views import PostList, PostDetail

# from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('posts/', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
]
