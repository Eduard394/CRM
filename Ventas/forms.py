# encoding:utf-8
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente


class ClientForm(forms.ModelForm):

	class Meta:
          model = Cliente
          fields = ('nombres', 'apellidos','cedula','activo','fecha_nacimiento','email','celular','direccion')


