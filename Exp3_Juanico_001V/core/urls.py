from django.urls import path
from .views import index, basededatos, crearUsuario, form_mod_usuario, form_del_usuario 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path ('', index, name = "index"),
    path ('basededatos', basededatos, name = "basededatos"),
    path ('crearUsuario/', crearUsuario, name = "crearUsuario"),
    path ('form_mod_usuario/<id>', form_mod_usuario, name = "form_mod_usuario"),
    path ('form_del_usuario/<id>', form_del_usuario, name = "form_del_usuario"), 
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)