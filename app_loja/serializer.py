from rest_framework import serializers
from app_loja.models import Cliente, Produto, Pedido

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    cliente = serializers.SlugRelatedField(
        queryset=Cliente.objects.all(),
        slug_field='nome'
    )
    #status = serializers.SerializerMethodField() # retorna o nome completo do status
    class Meta:
        model = Pedido
        fields = ['id', 'cliente', 'observacoes', 'data_pedido', 'status', 'produtos']

    #def get_status(self, obj): # retorna o nome completo do status
        #return obj.get_status_display()
