from django.contrib.auth.models import User
from .models import BookObject, BookAuthor


from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email")


class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    status = serializers.IntegerField()
    priority = serializers.IntegerField()
    description = serializers.CharField()
    created_at = serializers.DateTimeField()
    owner = serializers.CharField()
    pub_year = serializers.DateField()
    author = serializers.CharField()

    class Meta:
        model = BookObject
        fields = ("id", "title", "pub_year", "author","status","priority","description","created_at","owner")


class BookAuthorSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    description = serializers.CharField()
    born = serializers.DateField()
    died = serializers.DateField()

    class Meta:
        model = BookAuthor
        fields = ("id", "title", "description", "born", "died")
