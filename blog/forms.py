from django import forms
from .models import Post, Comment
# from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'image', 'image_alt')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

