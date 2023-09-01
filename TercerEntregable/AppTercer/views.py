from django.shortcuts import render
from django.http      import HttpResponse
from AppTercer.admin   import *
from AppTercer.models  import *
from AppTercer.forms   import *

# Create your views here.
def inicio(request):
    return render(request, "inicio/inicio.html",)

def clientes(request):
    return render(request, "clientes/inicio.html",)

def proveedores(request):
    return render(request, "proveedores/inicio.html",)

def productos(request):
    return render(request, "productos/inicio.html",)

def rubros(request):
    return render(request, "rubros/inicio.html",)

def pedidos(request):
    return render(request, "pedidos/inicio.html",)

## -- ALTAS -- ##

def AltaClienteForm(request):
    if request.method == 'POST':
        miForm = AltaCliente(request.POST)
        if miForm.is_valid():
            
            info = miForm.cleaned_data
            nuevoCliente = Cliente(nombre=info['nombre'],
                                   apellido=info['apellido'],
                                   fnasc=info['fnasc'],
                                   email=info['email'],
                                   dni=info['dni'],
                                   )
            nuevoCliente.save()
            return render(request, "clientes/inicio.html",{"mensaje": "Nuevo Cliente CREADO Exitosamente"})  
            
        else:
            return render(request, "clientes/inicio.html",{"mensaje": "Formulario Invalido"})  
    
    else:
        miForm = AltaCliente()
    
    return render(request, "clientes/alta.html",{"MiForm": miForm})  

##-------------------------------------------------------------------------------------------
def AltaProveedorForm(request):
    if request.method == 'POST':
        miForm = AltaProveedor(request.POST)
        if miForm.is_valid():
            
            info = miForm.cleaned_data
            nuevoProveedor = Proveedor(nombre=info['nombre'],
                                   contacto=info['contacto'],
                                   email=info['email'],
                                   cuit=info['cuit'],
                                   )
            nuevoProveedor.save()
            return render(request, "proveedores/inicio.html",{"mensaje": "Nuevo Proveedor CREADO Exitosamente"})  
            
        else:
            return render(request, "proveedores/inicio.html",{"mensaje": "Formulario Invalido"})  
    
    else:
        miForm = AltaProveedor()
    
    return render(request, "proveedores/alta.html",{"MiForm": miForm})  

##-------------------------------------------------------------------------------------------
def AltaProductoForm(request):
    if request.method == 'POST':
        miForm = AltaProducto(request.POST)
        if miForm.is_valid():
            
            info = miForm.cleaned_data
            nuevoProducto = Producto(nombre=info['nombre'],
                                   rubro=info['rubro'],
                                   precio=info['precio'],
                                   )
            nuevoProducto.save()
            return render(request, "productos/inicio.html",{"mensaje": "Nuevo Producto CREADO Exitosamente"})  
            
        else:
            return render(request, "productos/inicio.html",{"mensaje": "Formulario Invalido"})  
    
    else:
        miForm = AltaProducto()
    
    return render(request, "productos/alta.html",{"MiForm": miForm})  

##-------------------------------------------------------------------------------------------
def AltaRubroForm(request):
    if request.method == 'POST':
        miForm = AltaRubro(request.POST)
        if miForm.is_valid():
            
            info = miForm.cleaned_data
            nuevoRubro = RubroProd(nombre=info['nombre'],
                                   )
            nuevoRubro.save()
            return render(request, "rubros/inicio.html",{"mensaje": "Nuevo Rubro CREADO Exitosamente"})  
            
        else:
            return render(request, "rubros/inicio.html",{"mensaje": "Formulario Invalido"})  
    
    else:
        miForm = AltaRubro()
    
    return render(request, "rubros/alta.html",{"MiForm": miForm})  

##-------------------------------------------------------------------------------------------
def AltaPedidoForm(request):
    if request.method == 'POST':
        miForm = AltaPedido(request.POST)
        if miForm.is_valid():
            
            info = miForm.cleaned_data
            nuevoPedido = OrdenCompra(clientes=info['cliente'],
                                      producto=info['producto'],
                                      cantidad=info['cantidad'],
                                   )
            nuevoPedido.save()
            return render(request, "pedidos/inicio.html",{"mensaje": "Nuevo Pedido CREADO Exitosamente"})  
            
        else:
            return render(request, "pedidos/inicio.html",{"mensaje": "Pedido Invalido"})  
    
    else:
        miForm = AltaPedido()
    
    return render(request, "pedidos/alta.html",{"MiForm": miForm})  





## -- BUSQUEDAS -- ##
def BuscaClienteForm(request):
    return render(request, "clientes/busca.html")


def BuscaClienteResultForm(request):
    if request.GET["dni"]:
        dni      = request.GET["dni"]  
        nombre = Cliente.objects.get(dni=dni)
        if nombre:  
            return render(request, "clientes/result.html", {"A": nombre})
        else:
            return render( "clientes/result.html", {"mensaje": 'No existe ese Cliente'})
    else:
        return HttpResponse(f'No existe ese Cliente')
#------------------------------------------------------------------------------------------------
def BuscaProveedorForm(request):
    return render(request, "proveedores/busca.html")


def BuscaProveedorResultForm(request):
    if request.GET["cuit"]:
        cuit      = request.GET["cuit"]  
        nombre    = Proveedor.objects.get(cuit=cuit)
        if nombre:  
            return render(request, "proveedores/result.html", {"A": nombre})
        else:
            return render( "proveedores/result.html", {"mensaje": 'No existe ese Proveedor'})
    else:
        return HttpResponse(f'No existe ese Proveedor')
#------------------------------------------------------------------------------------------------
def BuscaProductoForm(request):
    return render(request, "productos/busca.html")


def BuscaProductoResultForm(request):
    if request.GET["nombre"]:
        nombre      = request.GET["nombre"]  
        proveedor    = Producto.objects.get(nombre=nombre)
        if proveedor:  
            return render(request, "productos/result.html", {"A": proveedor})
        else:
            return render( "productos/result.html", {"mensaje": 'No existe ese Producto'})
    else:
        return HttpResponse(f'No existe ese Producto')













## -- LISTADOS -- ##

def ListaClientesForm(request):
    lista = Cliente.objects.all()
    return render(request, 'clientes/lista.html', {'lista_clientes': lista})

def ListaProveedoresForm(request):
    lista = Proveedor.objects.all()
    return render(request, 'proveedores/lista.html', {'lista_proveedores': lista})

def ListaProductosForm(request):
    lista = Producto.objects.all()
    return render(request, 'productos/lista.html', {'lista_productos': lista})

def ListaRubrosForm(request):
    lista = RubroProd.objects.all()
    return render(request, 'rubros/lista.html', {'lista_rubros': lista})

def ListaPedidosForm(request):
    lista = OrdenCompra.objects.all()
    return render(request, 'pedidos/lista.html', {'lista_pedidos': lista})
