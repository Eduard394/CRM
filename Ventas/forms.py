# encoding:utf-8
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente,Producto,Venta


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



class NewVentaForm(forms.ModelForm):
	cliente = forms.ModelChoiceField(label=_(u'Asignar a usuario:'),
		widget=forms.Select(attrs={
			'size': 1, 'class': 'form-control'}),
		queryset=Cliente.objects.all(),
		empty_label=None)

	Producto = forms.ModelChoiceField(
		widget=forms.Select(attrs={
			'size': 1, 'class': 'form-control'}),
		queryset = Producto.objects.all(),
		empty_label=None)

	fecha= forms.DateField(
        label=_(u"Fecha de inicio"), widget=forms.TextInput(attrs={
            'class': 'form-control datepicker-min', 'placeholder': 'Fecha'}))


	"""estado = forms.ModelChoiceField(
		widget=forms.Select(attrs={
			'size': 1, 'class': 'form-control'}),
		queryset=EstadoActividad.objects.all(),
		empty_label=None)

	tipo_actividad = forms.ModelChoiceField(
		widget=forms.Select(attrs={
			'size': 1, 'class': 'form-control'}),
		queryset=TipoActividad.objects.all(),
		empty_label=None)"""


	class Meta:
		model = Venta
		fields = [
			'cliente',
			'producto',
			'fecha' ,
			'estado_pago'

		]

		labels = {
			'cliente' : 'Asignar a:  ',
			'producto' : 'Cuenta: ',
			'asunto' : 'Asunto',
			'descripcion' : 'Descripción',
			'fecha' : 'Fecha inicio'

		}


        def __init__(self, user=None, *args, **kwargs):
            super(NewVentaForm, self).__init__(*args, **kwargs)
            self.fields['cliente'].queryset = Cliente.objects.filter(clientes=user, activo = True) 
            self.fields['producto'].queryset = Producto.objects.all() | Producto.objects.filter(id=0).order_by('id')




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



