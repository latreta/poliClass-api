from rest_framework.viewsets import ModelViewSet

from salas.api.serializers import SalaSerializer
from salas.models import Sala


class SalasViewSet(ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

