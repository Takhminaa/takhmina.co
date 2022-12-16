from django.db import models


class Blogger(models.Model):
    name = models.CharField(max_length=50)


class Post(models.Model):
    user_id = models.ForeignKey(Blogger, related_name='blogger', on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(upload_to='postsimg', null=True)
    created_at = models.DateField(auto_now_add=True)
