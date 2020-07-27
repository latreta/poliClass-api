from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import Group

from users.models import Account


class UserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = ['id', 'username', 'email', 'groups', 'password', 'password2']


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
