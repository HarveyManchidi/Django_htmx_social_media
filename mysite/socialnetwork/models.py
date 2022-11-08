from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image

from django.urls import reverse
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='post_images')
    caption = models.CharField(max_length=128)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.caption

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('post-detail', args=[self.pk])


class Comment(models.Model):
    body = models.CharField(max_length=255)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(default=timezone.now)
#   likes = models.ManyToManyField(User, blank=True, related_name='comment_likes')
