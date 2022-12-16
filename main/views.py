from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model

from .models import Post

from .serializers import PostSerializers

User = get_user_model()

class PostViewSet(ModelViewSet):
    queryset= Post.objects.all()
    serializer_class = PostSerializers
