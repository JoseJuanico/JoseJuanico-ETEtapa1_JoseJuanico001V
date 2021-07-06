from django.shortcuts import redirect, render
from .models import Pago, Usuario
from .forms import UsuarioForm


# Create your views here.

def index (request):
    
    return render (request, 'index.html')


def basededatos(request):
    usuario = Usuario.objects.all() 
    return render (request, 'core/basededatos.html', context = {'datos': usuario})


def crearUsuario(request):
    if request.method == 'POST':
        usuario = UsuarioForm(request.POST)
        if usuario.is_valid(): 
            usuario.save()  
            return redirect('index') 
    else:
        usuario = UsuarioForm() 
    return render(request, 'core/form_crearusuario.html', {'usuario': usuario}) 
    


def form_mod_usuario(request, id): 
    usuario = Usuario.objects.get(rut = id) 

    datos = {
        'form': UsuarioForm(instance = usuario) 
    }
    if request.method == 'POST': 
        formulario = UsuarioForm(data = request.POST, instance = usuario) 
        if formulario.is_valid:
            formulario.save() 
            return redirect('basededatos')
    return render (request, 'core/form_mod_usuario.html', datos)
    
def form_del_usuario(request, id):
    usuario = Usuario.objects.get(rut = id)
    usuario.delete()
    return redirect('basededatos')
  