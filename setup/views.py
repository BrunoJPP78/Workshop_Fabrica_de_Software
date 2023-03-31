from rest_framework import viewsets
from setup.serializers import ToDoSerializer
from setup.models import ToDo

class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
