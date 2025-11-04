from rest_framework import viewsets
from .models import Galeria, Obra
from .serializers import GaleriaSerializer, ObraSerializer
from rest_framework.filters import SearchFilter, OrderingFilter

class GaleriaViewSet(viewsets.ModelViewSet):
    queryset = Galeria.objects.all().order_by('-created_at')
    serializer_class = GaleriaSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nombre', 'ubicacion']

class ObraViewSet(viewsets.ModelViewSet):
    queryset = Obra.objects.all().order_by('-created_at')
    serializer_class = ObraSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['obra', 'artista', 'tecnica']