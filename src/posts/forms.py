from django import forms
from django.forms.models import ModelForm
from .models import Post ,Comment



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

        labels = {
           'content' : '',
        }


class EditForm(forms.ModelForm):
    """Form definition for Edit."""

    class Meta:
        """Meta definition for Editform."""

        model = Post
        fields = ('title','overview','content')
