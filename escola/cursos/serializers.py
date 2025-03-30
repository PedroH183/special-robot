from rest_framework import serializers
from .models import Avaliacao, Curso

## Um serializer é apenas uma classe de intercambio entre model e JSON

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            # security issue
            # this will not be include into serializer output
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )

class CursoSerializer(serializers.ModelSerializer):
    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        )

