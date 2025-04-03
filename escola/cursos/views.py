from rest_framework import generics
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


class CursosAPIView(generics.ListCreateAPIView):
    """
    Views to Cursos Collection
    """

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacoesApiView(generics.ListCreateAPIView):
    """
    Views to Avaliacoes Collection
    """

    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer


class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Views de individuos
    """

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Views de individuos
    """

    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
