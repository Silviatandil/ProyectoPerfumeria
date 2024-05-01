from django.db import models

class perfume(models.Model):
    id= models.AutoField(primary_key=True)
    marca= models.CharField(max_length=100, verbose_name='Marca',null=True)
    nombre= models.CharField(max_length=100, verbose_name='Nombre',null=True)
    imagen= models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    descripcion= models.TextField(verbose_name='Descripcion', null=True)

    def __str__(self):
        fila = "Nombre:" + self.nombre + "-" + "Descripcion" + self.descripcion
        return fila
    
    def delete(self,using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

class maquillaje(models.Model):
    id= models.AutoField(primary_key=True)
    marca= models.CharField(max_length=100, verbose_name='Marca',null=True)
    nombre= models.CharField(max_length=100, verbose_name='Nombre',null=True)
    imagen= models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    descripcion= models.TextField(verbose_name='Descripcion', null=True)

class skinCare(models.Model):
    id= models.AutoField(primary_key=True)
    marca= models.CharField(max_length=100, verbose_name='Marca',null=True)
    nombre= models.CharField(max_length=100, verbose_name='Nombre',null=True)
    imagen= models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    descripcion= models.TextField(verbose_name='Descripcion', null=True)

class capilar(models.Model):
    id= models.AutoField(primary_key=True)
    marca= models.CharField(max_length=100, verbose_name='Marca',null=True)
    nombre= models.CharField(max_length=100, verbose_name='Nombre',null=True)
    imagen= models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    descripcion= models.TextField(verbose_name='Descripcion', null=True)

class accesorio(models.Model):
    id= models.AutoField(primary_key=True)
    marca= models.CharField(max_length=100, verbose_name='Marca',null=True)
    nombre= models.CharField(max_length=100, verbose_name='Nombre',null=True)
    imagen= models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    descripcion= models.TextField(verbose_name='Descripcion', null=True)