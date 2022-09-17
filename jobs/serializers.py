from rest_framework import serializers
from .models import (
    Replay,
    Blog,
    Index,
    About,
    Category,
)
from django.core.mail import send_mail


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"
        ordering = ["-date"]



class ReplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Replay
        fields = "__all__"


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class IndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Index
        fields = "__all__"

