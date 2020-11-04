from django.contrib.auth.models import User
from .models import BookObject, BookAuthor


from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email")


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookObject
        fields = ("id", "title", "pub_year", "author")


class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAuthor
        fields = ("id", "title", "born")
