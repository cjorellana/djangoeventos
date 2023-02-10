from django.db import models

# Create your models here.
class Evento(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    inicio = models.DateField()
    fin = models.DateField()
    diploma = models.BooleanField(default=1)
    foto = models.ImageField(upload_to='images/',null=True)
    descripcion = models.TextField()
    activo = models.BooleanField(default=1)

    def __str__(self):
        return self.nombre

class Pais(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)    
    dpi = models.CharField(max_length=13)
    nacimiento = models.DateField(null=True)
    pais = models.ForeignKey(Pais,on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        texto = "{0} {1}"
        return texto.format(self.nombre,self.apellido)

    
class Tipo_asignacion(models.Model):
    nombre = models.CharField(max_length=100)

class Catedratico(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)


