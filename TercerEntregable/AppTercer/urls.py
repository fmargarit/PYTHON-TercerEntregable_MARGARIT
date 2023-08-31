from django.urls import path
from AppTercer.views import *


urlpatterns = [
    
    path('inicio/', inicio, name='InicioURL'),
    path('', inicio, name='InicioURL'),
    
    path('clientes/', clientes, name='ClientesURL'),
    path('clientes/alta/', AltaClienteForm, name='ClientesAltaURL'),
    path('clientes/busca/', BuscaClienteForm, name='ClientesBuscaURL'),
    path('clientes/result/', BuscaClienteResultForm, name='ClientesBuscaResultURL'),
    path('clientes/lista/', ListaClientesForm, name='ClientesListaURL'),
    
    path('proveedores/', proveedores, name='ProveedoresURL'),
    path('proveedores/alta/', AltaProveedorForm, name='ProveedorAltaURL'),
    path('proveedores/lista/', ListaProveedoresForm, name='ProveedoresListaURL'),
    
    path('producto/', productos, name='ProductosURL'),
    path('producto/alta/', AltaProductoForm, name='ProductoAltaURL'),
    path('producto/lista/', ListaProductosForm, name='ProductosListaURL'),
    
    path('rubro/', rubros, name='RubrosURL'),
    path('rubro/alta/', AltaRubroForm, name='RubroAltaURL'),
    path('rubro/lista/', ListaRubrosForm, name='RubrosListaURL'),
    
    path('pedidos/', pedidos, name='PedidosURL'),
    path('pedidos/alta/', AltaPedidoForm, name='PedidoAltaURL'),
    path('pedidos/lista/', ListaPedidosForm, name='PedidosListaURL'),
]