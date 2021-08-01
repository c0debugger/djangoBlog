from django import forms
from django.forms.models import ModelForm
from .models import Post ,Comment
from django.forms import  Textarea


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

        labels = {
           'content' : '',
        }

        widgets = {
            'content': Textarea(attrs={'cols': 1, 'rows': 2}),
        }


class EditForm(forms.ModelForm):
    """Form definition for Edit."""

    class Meta:
        """Meta definition for Editform."""

        model = Post
        fields = ('title','overview','content')
