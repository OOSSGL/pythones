"""Posts forms."""

# Django
from django import forms

# Models
from posts.models import Post


class PostForm(forms.ModelForm):
    """Post model from."""

    class Meta:
        """Form settings."""

        model = Post
        fields = ('user', 'profile', 'tittle', 'photo')
