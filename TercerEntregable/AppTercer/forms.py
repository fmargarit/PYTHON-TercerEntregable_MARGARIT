from django import forms
from AppTercer.models import Proveedor, RubroProd

class AltaCliente(forms.Form):
    nombre   = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    fnasc    = forms.DateField(required=True)
    email    = forms.EmailField(required=True)
    dni      = forms.IntegerField(required=True)
    
class AltaProveedor(forms.Form):
    nombre   = forms.CharField(required=True)
    contacto = forms.CharField(required=True)
    email    = forms.EmailField(required=True)
    cuit     = forms.IntegerField(required=True)

class AltaRubro(forms.Form):
    nombre   = forms.CharField(required=True)
    
class AltaProducto(forms.Form):
    nombre   = forms.CharField(required=True)
    proveedor= forms.ChoiceField(widget=forms.Select(choices=Proveedor.objects.all()))
    rubro    = forms.ChoiceField(widget=forms.Select(choices=RubroProd.objects.all()))
    precio   = forms.DecimalField(required=True)
    
class AltaPedido(forms.Form):
    comprador= forms.CharField(required=True)
    producto = forms.CharField(required=True)
    cantidad = forms.DecimalField(required=True)