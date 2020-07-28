from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rolepermissions.checkers import has_permission
from rest_framework_simplejwt.authentication import JWTAuthentication

from aulas.api.serializers import AulaSerializer
from aulas.models import Aula


class AulasViewSet(ModelViewSet):
    queryset = Aula.objects.all()
    serializer_class = AulaSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = {JWTAuthentication}

    def list(self, request, *args, **kwargs):
        user = request.user
        if has_permission(user, 'ver_aulas'):
            return super(AulasViewSet, self).list(request, *args, **kwargs)

        return Response(status=status.HTTP_403_FORBIDDEN)