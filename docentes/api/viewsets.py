from rest_framework.viewsets import ModelViewSet

from docentes.api.serializers import DocenteSerializer
from docentes.models import Docente


class DocentesViewSet(ModelViewSet):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer
