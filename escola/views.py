from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculaAlunoSerializer, ListaAlunosMatriculadosCursoSerializer

class AlunosViewsSet (viewsets.ModelViewSet):
    '''Exibindo todos os alunos e alunas'''
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursosViewSet (viewsets.ModelViewSet):
    '''Exibindo todos os Cursos'''
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet (viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculasAluno(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculaAlunoSerializer

class ListaAlunosMatriculados(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosCursoSerializer