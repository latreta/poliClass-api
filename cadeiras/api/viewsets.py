from rest_framework.viewsets import ModelViewSet

from cadeiras.api.serializers import CadeiraSerializer
from cadeiras.models import Cadeira
from policlass.custom_decorators import can_access_with_role


class CadeirasViewSet(ModelViewSet):
    queryset = Cadeira.objects.all()
    serializer_class = CadeiraSerializer

    @can_access_with_role('funcionario')
    def create(self, request, *args, **kwargs):
        return super(CadeirasViewSet, self).create(request, *args, **kwargs)
