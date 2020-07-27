from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from users.api.serializers import UserSerializer, GroupSerializer
from users.models import Account, AccountManager


class UserViewSet(ModelViewSet):
    queryset = Account.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        user = Account.objects.create_user(
            email=request.data['email'],
            username=request.data['username'],
            password=request.data['password'],
            password2=request.data['password2']
        )
        return user

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        # Update user data like change password or something
        return Response(status=status.HTTP_403_FORBIDDEN)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_403_FORBIDDEN)


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
