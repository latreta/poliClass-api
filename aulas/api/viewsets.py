from rest_framework.viewsets import ModelViewSet

from aulas.api.serializers import AulaSerializer
from aulas.models import Aula


class AulasViewSet(ModelViewSet):
    queryset = Aula.objects.all()
    serializer_class = AulaSerializer

