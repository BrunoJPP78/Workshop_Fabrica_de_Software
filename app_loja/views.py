from django.db.models import Count
from rest_framework import viewsets
from app_loja.models import Cliente, Produto, Pedido
from app_loja.serializer import ClienteSerializer, ProdutoSerializer, PedidoSerializer

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer




