from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^$',home,name="home"),
		url(r'^cursos/(\d+)/$',cursos,name="cursos"),
		url(r'^login/$',login,name="login"),
		url(r'^registro/$',registro,name="registro"),
		url(r'^salir/$',salir,name="salir"),

		url(r'^cuentaUsuario/(\d+)/$',cuentaUsuario,name="cuentaUsuario"),
		url(r'^misCursos/(\w+)/$',misCursos,name="misCursos"),
	]