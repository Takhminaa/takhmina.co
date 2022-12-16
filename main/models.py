from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    user_id = models.ForeignKey(User, related_name='blogger', on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(upload_to='postsimg', null=True)
    created_at = models.DateField(auto_now_add=True)

