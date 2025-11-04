from rest_framework import serializers
from .models import Galeria, Obra

class ObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obra
        fields = '__all__'

class GaleriaSerializer(serializers.ModelSerializer):
    obras = ObraSerializer(many=True, read_only=True)
    class Meta:
        model = Galeria
        fields = '__all__'
