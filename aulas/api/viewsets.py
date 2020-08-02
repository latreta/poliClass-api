from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rolepermissions.checkers import has_object_permission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rolepermissions.decorators import has_role_decorator

from aulas.api.serializers import AulaSerializer
from aulas.models import Aula
from policlass.custom_decorators import can_access_with_role


class AulasViewSet(ModelViewSet):
    queryset = Aula.objects.all()
    serializer_class = AulaSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = {JWTAuthentication}

    @can_access_with_role('funcionario')
    def create(self, request, *args, **kwargs):
        return super(AulasViewSet, self).create(request, *args, **kwargs)

    @can_access_with_role('funcionario')
    def update(self, request, *args, **kwargs):
        return super(AulasViewSet, self).update(request, *args, **kwargs)

    @can_access_with_role('funcionario')
    def destroy(self, request, *args, **kwargs):
        return super(AulasViewSet, self).destroy(request, *args, **kwargs)
