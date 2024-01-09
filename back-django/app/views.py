from rest_framework import viewsets
from .models import MiModelo
from .serializers import MiModeloSerializer

class MiModeloViewSet(viewsets.ModelViewSet):
    queryset = MiModelo.objects.all()
    serializer_class = MiModeloSerializer