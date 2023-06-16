from django.db import models

# Create your models here.
def path_file_name(instance, filename):
   return os.path.join('logos', instance.nombre, filename)

class Textos(models.Model):    
    titulo = models.CharField(max_length=200)
    acercaDe = models.TextField()
    imagen = models.ImageField(upload_to='textos')

    def __str__(self):
        return self.titulo
class Logos(models.Model):
    nombre = models.CharField(max_length=200)
    nombre_corto = models.CharField(max_length=200)
    logo = models.ImageField(upload_to=path_file_name)

    def __str__(self):
        return self.nombre

class PieDePagina(models.Model):    
    titulo = models.CharField(max_length=200)
    email = models.CharField(max_length=200, blank=True, null=True)
    tel = models.CharField(max_length=200, blank=True, null=True)
    facebook = models.CharField(max_length=200, blank=True, null=True)
    youtube = models.CharField(max_length=200, blank=True, null=True)
    instagram = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.titulo
class Colaborador(models.Model):    
    nombre = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='colaboradores')
    descripcion = models.TextField()
    enlace = models.URLField(blank=True, null=True)  # Opcional, en caso de que tengan un perfil o página externa

    def __str__(self):
        return self.nombre
