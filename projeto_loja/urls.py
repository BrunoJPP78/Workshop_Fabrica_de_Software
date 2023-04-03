from django.contrib import admin
from django.urls import path, include
from app_loja.views import ClientesViewSet, ProdutoViewSet, PedidoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clientes', ClientesViewSet, basename='Cliente')
router.register('produtos', ProdutoViewSet, basename='Produtos')
router.register('pedidos', PedidoViewSet, basename='Pedidos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
