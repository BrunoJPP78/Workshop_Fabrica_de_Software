from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'nome_curso', 'codigo_curso', 'descricao', 'nivel']
class MatriculaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = [] #nao vai excluir nada, ou seja, mostrará todos

class ListaMatriculaAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    matricula = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'matricula']

    def get_matricula(self, obj):
        return obj.get_matricula_display()

class ListaAlunosMatriculadosCursoSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_nome']
