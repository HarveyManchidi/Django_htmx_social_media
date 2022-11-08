from django.forms import ModelForm
from .models import Post, Comment


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'caption']


class PostUpdateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'caption']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
