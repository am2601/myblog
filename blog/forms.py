from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'post_image', 'image_alt')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

