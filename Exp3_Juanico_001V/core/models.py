from django.db import models


# Create your models here.
class Pago(models.Model):
    idPago= models.IntegerField(primary_key = True, verbose_name='Id pago') 
    tipo = models.CharField(max_length = 20, verbose_name = 'Tipo de moneda')

    def __str__(self):
        return self.tipo

class Usuario(models.Model):
    rut = models.CharField (max_length = 10,primary_key = True, verbose_name = 'Rut del usuario')
    nombre = models.CharField (max_length = 50, verbose_name = 'Nombre Completo')
    telefono = models.CharField (max_length = 50, verbose_name = 'Teléfono')
    direccion = models.CharField (max_length = 50, verbose_name = 'Dirección')
    correo = models.EmailField (max_length = 50,verbose_name = 'Correo electrónico')
    pais = models.CharField (max_length = 50, verbose_name = 'País')
    contrasena = models.CharField (max_length = 9, verbose_name = 'contraseña')
    tipo = models.ForeignKey (Pago, on_delete=models.CASCADE) 
    foto = models.ImageField (upload_to = 'images/', null = True, blank = True)
   
    def __str__(self): # metodo toString
        return self.rut

