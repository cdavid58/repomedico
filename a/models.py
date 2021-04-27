from django.db import models


class Usuario(models.Model):
	nombre = models.CharField(max_length=20,blank=True,null=True)
	apellido = models.CharField(max_length=20,null=True)
	telefono = models.CharField(max_length=10,blank=True,null=True)
	email = models.EmailField()
	bloqueado = models.BooleanField(default=False)
	clave = models.CharField(max_length=16,default='1234')
	dia = models.CharField(max_length=2,default="",null=True,blank=True)
	mes = models.CharField(max_length=15,default="",null=True,blank=True)
	anio = models.CharField(max_length=4,default="",null=True,blank=True)

	def __str__(self):
		return self.email


class Categorias(models.Model):
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre


class Permisos(models.Model):
	permiso = models.CharField(max_length=100,default="no")
	usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)



class Curso(models.Model):
	video = models.FileField(upload_to="videos")
	masVisto = models.BooleanField(default=False)
	cate = models.ForeignKey(Categorias,on_delete=models.CASCADE)
	intro = models.BooleanField(default=False)
	titulo = models.CharField(max_length=100,default='')
	subtitulo = models.CharField(max_length=100,default='',null=True)
	click = models.CharField(max_length=100,default=0,null=True)

	def __str__(self):
		return self.titulo











