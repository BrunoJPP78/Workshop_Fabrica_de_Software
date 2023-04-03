from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    cpf =  models.CharField(max_length=11)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=100)
    num_telefone = models.CharField(max_length=11)

    def __str__(self):
        return self.nome

    def cliente_nome(self):
        return self.nome

class Produto(models.Model):
    TIPO = (
        ('Periférico', 'Periféricos'),
        ('Eletrônico', 'Eletrônicos'),
        ('Hardware', 'Hardwares'),
        ('Celular', 'Celulares'),
    )

    nome_produto = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    preco = models.CharField(max_length=20)
    tipo = models.CharField(max_length=30, choices=TIPO, blank=False, null=False)

    def __str__(self):
        return f"{self.nome_produto} | {self.preco}"

class Pedido(models.Model):
    STATUS = (
        ('REALIZADO', 'Pedido realizado'),
        ('PREPARAÇÃO', 'Pedido em preparação'),
        ('ENTREGA', 'Saiu para entrega'),
    )
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE, related_name='pedidos')
    observacoes = models.CharField(max_length=300, null=False, blank=False)
    data_pedido = models.DateTimeField()
    status = models.CharField(max_length=30, choices=STATUS, blank=False, null=False)
    produtos = models.ManyToManyField(Produto)

    def __str__(self):
        return self.cliente.nome
