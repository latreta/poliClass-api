from django.contrib.auth.models import Group
from django.http import HttpResponse
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
        return HttpResponse(user)


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
