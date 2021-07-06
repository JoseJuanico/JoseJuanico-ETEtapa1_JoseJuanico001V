from django import forms
from django.db.models.base import Model
from django.forms import ModelForm, widgets
from .models import Usuario

class UsuarioForm(ModelForm): 
	class Meta:
		model = Usuario 
		fields = ['rut', 'nombre', 'telefono', 'direccion', 'correo', 'pais', 'contrasena', 'tipo', 'foto']

		labels = { 
			'rut': 'Ingrese el rut (EJ.10637553-2)',  
			'nombre': 'Ingrese el nombre',
			'telefono': 'Ingrese teléfono',
			'direccion': 'Ingrese dirección',
			'correo': 'Ingrese el correo electrónico',
			'pais': 'Ingrese país',
			'contrasena': 'Ingrese la contraseña',
			'tipo': 'Ingrese el tipo de Pago',
			'foto': 'Ingrese foto',
			'editar': 'Editar',
			'eliminar': 'Borrar de base de datos',
		}

		widgets = {
			'rut': forms.TextInput(
				attrs = {
					'class': 'form-control',
					'placeholder': 'Rut sin puntos...',
					'id': 'lrut',
					'name': 'lrut',
				}
			),
			'nombre': forms.TextInput(
				attrs = {
					'class': 'form-control',
					'placeholder': 'Nombres...',
					'id': 'lnombre',
					'name': 'lnombre',
				}
			),
			'telefono': forms.TextInput(
				attrs = {
					'class': 'form-control',
					'placeholder': 'Teléfono...',
					'id': 'ltelefono',
					'name': 'ltelefono',
				}
			),
			'direccion': forms.TextInput(
				attrs = {
					'class': 'form-control',
					'placeholder': 'Dirección...',
					'id': 'ldireccion',
					'name': 'ldireccion',
				}
			),
			'correo': forms.EmailInput(
				attrs = {
					'class': 'form-control',
					'placeholder': 'Correo electrónico...',
					'id': 'lcorreo',
					'name': 'lcorreo',
				}
			),
			'pais': forms.TextInput(
				attrs = {
					'class': 'form-control',
					'placeholder': 'País...',
					'id': 'lpais',
					'name': 'lpais',
				}
			),
			'contrasena': forms.PasswordInput(
				attrs = {
					'class': 'form-control',
					'placeholder': 'Máx. 9 caracteres...',
					'id': 'lpassword1',
					'name': 'lpassword1',
				}
			),
			'tipo': forms.Select(
				attrs = {
					'class': 'form-control',
					'id': 'tipo',
				}
			),
			'foto': forms.ClearableFileInput(
				attrs = {
					'class': 'form-control',
					'id': 'foto'

				}
			)
		}
