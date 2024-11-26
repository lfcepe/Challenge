from django.db import models

# Create your models here.
class Retos(models.Model):
    reto = models.CharField(null = False, max_length=100)
    descripcion = models.CharField(null= False, max_length=400)
    puntos = models.IntegerField(default = 0 , null = False)

    def __str__(self) -> str:
        return self.reto
    
class Retosrespuesta (models.Model):
    usuario = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    reto = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    imagenusuario = models.ImageField(upload_to='pruebas_imagen')
    ESTADO = {
        ('APROVADO', 'APROVADO'),
        ('PENDIENTE', 'PENDIENTE')
    }
    estado = models.CharField(max_length=50, choices= ESTADO, null = False)

    
class Poemas (models.Model):
    usuario = models.ForeignKey("User", on_delete=models.CASCADE)
    titulopoema = models.CharField(null = False, max_length=90)
    rima = models.TextField(null = False, max_length= 1000)
    puntospoemas = models.IntegerField(default=0, null= True)

    def __str__(self) -> str:
        return self.titulopoema


class Dibujos (models.Model):
    usuario = models.ForeignKey("User", on_delete=models.CASCADE)
    nombredibujo = models.CharField(null=False, max_length=90)
    imagen = models.ImageField(upload_to='dibujos_imagenes')
    puntosdibujo = models.IntegerField(default=0, null= True)

    def __str__(self):
        return self.nombredibujo
    

class Rankings (models.Model):
    usuario = models.ForeignKey("User", on_delete=models.CASCADE)
    puntostotales = models.IntegerField(default= 0, null= False)

    def  __str__(self) -> str:
        return self.usuario