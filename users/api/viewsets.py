from django.http import HttpResponse
from rest_framework.viewsets import GenericViewSet
from rolepermissions.roles import assign_role

from users.api.serializers import UserSerializer
from users.models import Account


class UserViewSet(GenericViewSet):
    queryset = Account.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        user = Account.objects.create_user(
            email=request.data['email'],
            username=request.data['username'],
            password=request.data['password'],
            password2=request.data['password2']
        )
        assign_role(user, 'funcionario')
        return HttpResponse(user)

