from rest_framework import serializers
from watchrank.models import Programa

class ProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programa
        fields = ['titulo', 'tipo', 'data_lancamento', 'likes']