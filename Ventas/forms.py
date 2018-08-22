from django import forms

from .models import Cliente


class ClientForm(forms.ModelForm):

	class Meta:
          model = Cliente
          fields = ('nombres', 'apellidos','cedula','activo','fecha_nacimiento','email','celular','direccion')