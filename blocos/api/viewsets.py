from rest_framework.viewsets import ModelViewSet

from blocos.api.serializers import BlocoSerializer
from blocos.models import Bloco


class BlocosViewSet(ModelViewSet):
    queryset = Bloco.objects.all()
    serializer_class = BlocoSerializer
