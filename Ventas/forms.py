# encoding:utf-8
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente,Producto,Venta


##### Forms vistas basadas en Funciones ############

class ClientForm(forms.ModelForm):

	class Meta:
          model = Cliente
          fields = ('nombres', 'apellidos','cedula','activo','fecha_nacimiento','email','celular','direccion')

class ProductoForm(forms.ModelForm):

	class Meta:
          model = Producto
          fields = ('nombre','descripcion', 'cantidad','precio_unitario')

class VentaForm(forms.ModelForm):

	class Meta:
          model = Venta
          fields = ('cliente','producto', 'cantidad','precio_unitario','precio_total','estado_pago')

#####  FIN   Forms vistas basadas en Funciones ############



##### Forms vistas basadas en Clases ############




######### from Nuevos clientes
class NewClientForm(forms.ModelForm):

	nombres = forms.CharField(
	max_length=60, required=True, label='Nombres',
	widget=forms.TextInput(attrs={
		'class': 'form-control', 'placeholder': '',
		'required': 'required'}))

	apellidos = forms.CharField(
	max_length=60, required=True, label='Apellidos',
	widget=forms.TextInput(attrs={
		'class': 'form-control', 'placeholder': '',
		'required': 'required'}))

	cedula = forms.CharField(
	max_length=60, required=True, label='Identificacion',
	widget=forms.TextInput(attrs={
		'class': 'form-control', 'placeholder': 'CC',
		'required': 'required'}))

	fecha_nacimiento= forms.DateField(
        label=_(u"Fecha de Nacimiento"), widget=forms.TextInput(attrs={
            'class': 'form-control datepicker-min', 'placeholder': '07/08/1950'}))


	email = forms.EmailField(
		label='Correo electrónico', required=False	,
		widget=forms.TextInput(attrs={
			'class': 'form-control', 'placeholder': 'Correo electrónico',
			'required': 'required', 'type': 'email'}))


	direccion = forms.CharField(
	label=_(u'Dirección'), required=False,
	widget=forms.Textarea(attrs={
		'rows': 1, 'class': 'form-control',
		'placeholder': _(u'Dirección')}))	


	celular= forms.CharField(
	max_length=10, required=False, label='Telefono',
	widget=forms.TextInput(attrs={
		'class': 'form-control', 'placeholder': 'Celular',
		'required': 'required'}))

	class Meta:
		model = Cliente
		fields = [
			'nombres',
			'apellidos',
			'cedula',
			'fecha_nacimiento',
			'email',
			'direccion',
			'celular'  ,
			

		]

		labels = {
			
		}



#### FORM para Nuevos productos
class NewProductoForm(forms.ModelForm):

	nombre = forms.CharField(
	max_length=30, required=True, label='Nombre',
	widget=forms.TextInput(attrs={
		'class': 'form-control', 'placeholder': '',
		'required': 'required'}))

	descripcion = forms.CharField(
	max_length=30, required=True, label='Descripcion',
	widget=forms.TextInput(attrs={
		'class': 'form-control', 'placeholder': '',
		'required': 'required'}))

	cantidad = forms.IntegerField(
	required=True, label='Cantidad',
	widget=forms.TextInput(attrs={
		'class': 'form-control', 'placeholder': 'Cantidad',
		'required': 'required'}))


	precio_unitario= forms.IntegerField(
	required=True, label='Precio Unitario',
	widget=forms.TextInput(attrs={
		'class': 'form-control', 'placeholder': 'Precio Unitario',
		'required': 'required'}))


	class Meta:
		model = Producto
		fields = [
			'nombre',
			'descripcion',
			'cantidad',
			'precio_unitario',
		]

		labels = {
			
		}



#######  FORM para Ventas #################
class NewVentaForm(forms.ModelForm):
	cliente = forms.ModelChoiceField(label=_(u'Asignar a usuario:'),
		widget=forms.Select(attrs={
			'size': 1, 'class': 'form-control'}),
		queryset=Cliente.objects.all(),
		empty_label=None)

	producto = forms.ModelChoiceField(
		widget=forms.Select(attrs={
			'size': 1, 'class': 'form-control'}),
		queryset = Producto.objects.all(),
		empty_label=None)

	fecha= forms.DateField(
        label=_(u"Fecha "), widget=forms.TextInput(attrs={
            'class': 'form-control datepicker-min', 'placeholder': 'Fecha'}))

	precio_unitario= forms.IntegerField(
	required=True, label='Cantidad',
	widget=forms.TextInput(attrs={
		'class': 'form-control', 'placeholder': 'Precio Unitario',
		'required': 'required'}))

	cantidad = forms.IntegerField(
	required=True, label='Cantidad',
	widget=forms.TextInput(attrs={
		'class': 'form-control', 'placeholder': 'Cantidad',
		'required': 'required'}))

	precio_total = forms.IntegerField(
	required=True, label='Cantidad',
	widget=forms.TextInput(attrs={
		'class': 'form-control', 'placeholder': 'Precio Total',
		'required': 'required'}))

	class Meta:
		model = Venta
		fields = [
			'cliente',
			'producto',
			'fecha' ,
			'precio_unitario',
			'cantidad' ,
			'precio_total' ,
		]

		labels = {
		}


        def __init__(self, user=None, *args, **kwargs):
            super(NewVentaForm, self).__init__(*args, **kwargs)
            self.fields['cliente'].queryset = Cliente.objects.all()
            self.fields['producto'].queryset = Producto.objects.all()





##### FIN     Forms vistas basadas en Clases ############