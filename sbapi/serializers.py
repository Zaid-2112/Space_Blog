from rest_framework import serializers
from blog.models import Post, Categorie


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id', 'title']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'overview','time_upload', 'auther', 'categories', 'read']
