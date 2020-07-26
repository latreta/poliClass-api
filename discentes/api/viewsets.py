from rest_framework.viewsets import ModelViewSet

from discentes.api.serializers import DiscenteSerializer
from discentes.models import Discente


class DiscentesViewSet(ModelViewSet):
    queryset = Discente.objects.all()
    serializer_class = DiscenteSerializer
