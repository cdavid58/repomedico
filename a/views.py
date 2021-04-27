from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

def salir(request):
	del request.session['usuario']
	return redirect('/')


def login(request):
	print('Entre al login')
	if request.method == 'POST':
		print(request.POST.get('email'))
		print(request.POST.get('pass'))
		try:
			usr = Usuario.objects.get(email=request.POST.get('email'),clave = request.POST.get('pass'))
		except Usuario.DoesNotExist:
			print('Error')
			usr = None

		if usr is not None:
			request.session['usuario'] = usr.pk
			return redirect(request.session['location'])
	return redirect('cursos')

def registro(request):
	cat = Categorias.objects.all()
	error = False
	if request.method == 'POST':
		try:
			usr = Usuario.objects.get(email=request.POST.get('email'))
		except Usuario.DoesNotExist:
			usr = None
		if usr is not None:
			error = True
		else:
			Usuario(
				telefono = request.POST.get('tlf'),
				email = request.POST.get('email'),
				clave = request.POST.get('pass'),
				dia = request.POST.get('dia'),
				mes = request.POST.get('mes'),
				anio = request.POST.get('anio')				
			).save()
			usuario = Usuario.objects.get(email=request.POST.get('email'))
			request.session['usuario'] = usuario.pk
			return redirect(request.session['location'])

	return render(request,'registro.html',{'error':error,'categoria':cat})

def home(request):
	request.session['location'] = '/'
	cat = Categorias.objects.all()
	return render(request,'index.html',{'categoria':cat})

def cursos(request,pk):
	request.session['curso'] = pk

	if request.is_ajax():
		ide = request.GET.get('id')
		try:
			p = Permisos.objects.filter(usuario= Usuario.objects.get(pk=request.session['usuario']), permiso = Categorias.objects.get(pk=request.GET.get('id')).nombre)
		except Permisos.DoesNotExist:
			p = None

		if p is not None:
			return HttpResponse(request.session['usuario'])
		else:
			Permisos(
				permiso = Categorias.objects.get(pk=request.GET.get('id')).nombre,
				usuario = Usuario.objects.get(pk=request.session['usuario'])
			).save()
			return HttpResponse(request.session['usuario'])
			
	request.session['location'] = '/cursos/'+str(pk)

	if int(pk) == 0:
		cur = Curso.objects.filter(intro=True)
		return render(request,'cursos.html',{'curso':cur})
	cat = Categorias.objects.all()
	cur = Curso.objects.filter(cate=Categorias.objects.get(pk=pk),intro=True)
	for i in cur:
		print(i.video)
	return render(request,'cursos.html',{'categoria':cat,'curso':cur})

def cuentaUsuario(request,pk):
	if 'usuario' in request.session:
		permiso = Permisos.objects.filter( usuario=Usuario.objects.get(pk=request.session['usuario']) )
		return render(request,'cuenta/usuario.html',{'permisos':permiso})
	return redirect('/')


def misCursos(request,pk):
	if 'usuario' in request.session:
		cat = Categorias.objects.get(nombre=pk)
		cursos = Curso.objects.filter(cate=Categorias.objects.get(pk=cat.pk))
		permiso = Permisos.objects.filter( usuario=Usuario.objects.get(pk=request.session['usuario']) )
		return render(request,'cuenta/cursos.html',{'c':cat,'cursos':cursos,'permisos':permiso})





