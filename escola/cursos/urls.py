from django.urls import path
from .views import CursosAPIView, AvaliacoesApiView, CursoAPIView, AvaliacaoAPIView

urlpatterns = [
    path("cursos/", CursosAPIView.as_view(), name="curso"),
    path("cursos/<int:pk>", CursoAPIView.as_view(), name="cursos"),
    path("avaliacoes/", AvaliacoesApiView.as_view(), name="avaliacoes"),
    path("avaliacao/<int:pk>", AvaliacaoAPIView.as_view(), name="avaliacao"),
]
