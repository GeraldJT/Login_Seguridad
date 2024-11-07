from django.urls import path
from . import views

urlpatterns = [
    path('', views.hola_mundo, name='login.html'),
    # URLs de usuarios
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/editar/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/eliminar/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('usuarios/<int:usuario_id>/asignar_rol/', views.asignar_rol_usuario, name='asignar_rol_usuario'),
  

    # URLs de roles
    path('roles/', views.lista_roles, name='lista_roles'),
    path('roles/crear/', views.crear_rol, name='crear_rol'),
    path('roles/editar/<int:rol_id>/', views.editar_rol, name='editar_rol'),
    path('roles/eliminar/<int:rol_id>/', views.eliminar_rol, name='eliminar_rol'),
    path('roles/<int:rol_id>/asignar_funcion/', views.asignar_funcion_rol, name='asignar_funcion_rol'),

    # URLs de funciones
    path('funciones/', views.lista_funciones, name='lista_funciones'),
    path('funciones/crear/', views.crear_funcion, name='crear_funcion'),
    path('funciones/editar/<int:funcion_id>/', views.editar_funcion, name='editar_funcion'),
    path('funciones/eliminar/<int:funcion_id>/', views.eliminar_funcion, name='eliminar_funcion'),
]
