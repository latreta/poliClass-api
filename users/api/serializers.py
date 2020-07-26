from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User, Group


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
