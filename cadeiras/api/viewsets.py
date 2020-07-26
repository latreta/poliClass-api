from rest_framework.viewsets import ModelViewSet

from cadeiras.api.serializers import CadeiraSerializer
from cadeiras.models import Cadeira


class CadeirasViewSet(ModelViewSet):
    queryset = Cadeira.objects.all()
    serializer_class = CadeiraSerializer
