from django.urls import path
from AppTercer.views import *


urlpatterns = [
    
    path('inicio/', inicio, name='InicioURL'),
    path('', inicio, name='InicioURL'),
    
    path('clientes/', clientes, name='ClientesURL'),
    path('clientes/alta/', AltaClienteForm, name='ClientesAltaURL'),
    
    path('proveedores/', proveedores, name='ProveedoresURL'),
    path('proveedores/alta/', AltaProveedorForm, name='ProveedorAltaURL'),
    
    path('producto/', productos, name='ProductosURL'),
    path('producto/alta/', AltaProductoForm, name='ProductoAltaURL'),
    
    path('rubro/', rubros, name='RubrosURL'),
    path('rubro/alta/', AltaRubroForm, name='RubroAltaURL'),
    
    path('pedidos/', pedidos, name='PedidosURL'),
    path('pedidos/alta/', AltaPedidoForm, name='PedidoAltaURL'),
]