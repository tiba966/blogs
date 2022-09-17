from django import forms

from .models import Blog


class StoryDetailForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
        exclude = ("id",)
