from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Funcion, Rol, Usuario, RolFuncion, UsuarioRol

def hola_mundo(request):
    return render(request,'login.html')

# Listar Funciones
def lista_funciones(request):
    funciones = Funcion.objects.all()
    return render(request, 'funciones/lista_funciones.html', {'funciones': funciones})

# Crear Funcion
def crear_funcion(request):
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        Funcion.objects.create(descripcion=descripcion)
        messages.success(request, 'Función creada exitosamente.')
        return redirect('lista_funciones')
    return render(request, 'funciones/crear_funcion.html')

# Editar Funcion
def editar_funcion(request, funcion_id):
    funcion = get_object_or_404(Funcion, id=funcion_id)
    if request.method == 'POST':
        funcion.descripcion = request.POST.get('descripcion')
        funcion.save()
        messages.success(request, 'Función actualizada correctamente.')
        return redirect('lista_funciones')
    return render(request, 'funciones/editar_funcion.html', {'funcion': funcion})

# Eliminar Funcion
def eliminar_funcion(request, funcion_id):
    funcion = get_object_or_404(Funcion, id=funcion_id)
    funcion.delete()
    messages.success(request, 'Función eliminada correctamente.')
    return redirect('lista_funciones')

# Listar Roles
def lista_roles(request):
    roles = Rol.objects.all()
    return render(request, 'roles/lista_roles.html', {'roles': roles})

# Crear Rol
def crear_rol(request):
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        Rol.objects.create(descripcion=descripcion)
        messages.success(request, 'Rol creado exitosamente.')
        return redirect('lista_roles')
    return render(request, 'roles/crear_rol.html')

# Editar Rol
def editar_rol(request, rol_id):
    rol = get_object_or_404(Rol, id=rol_id)
    if request.method == 'POST':
        rol.descripcion = request.POST.get('descripcion')
        rol.save()
        messages.success(request, 'Rol actualizado correctamente.')
        return redirect('lista_roles')
    return render(request, 'roles/editar_rol.html', {'rol': rol})

# Eliminar Rol
def eliminar_rol(request, rol_id):
    rol = get_object_or_404(Rol, id=rol_id)
    rol.delete()
    messages.success(request, 'Rol eliminado correctamente.')
    return redirect('lista_roles')

# Listar Usuarios
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    print(usuarios +"jaja")
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})

# Crear Usuario
def crear_usuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        user = request.POST.get('user')
        password = request.POST.get('password')
        
        if not Usuario.objects.filter(user=user).exists():
            Usuario.objects.create(nombre=nombre, user=user, password=password)
            messages.success(request, 'Usuario creado exitosamente.')
            return redirect('lista_usuarios')
        else:
            messages.error(request, 'El nombre de usuario ya existe.')
    
    return render(request, 'log/usuarios/crear_usuario.html')

# Editar Usuario
def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        usuario.nombre = request.POST.get('nombre')
        usuario.user = request.POST.get('user')
        usuario.password = request.POST.get('password')
        usuario.save()
        messages.success(request, 'Usuario actualizado correctamente.')
        return redirect('lista_usuarios')
    
    return render(request, 'usuarios/editar_usuario.html', {'usuario': usuario})

# Eliminar Usuario
def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.delete()
    messages.success(request, 'Usuario eliminado correctamente.')
    return redirect('lista_usuarios')

def asignar_funcion_rol(request, rol_id):
    rol = get_object_or_404(Rol, id=rol_id)
    funciones = Funcion.objects.all()
    
    if request.method == 'POST':
        funcion_id = request.POST.get('funcion')
        funcion = get_object_or_404(Funcion, id=funcion_id)
        RolFuncion.objects.create(rol=rol, funcion=funcion)
        messages.success(request, 'Función asignada exitosamente al rol.')
        return redirect('lista_roles')
    
    return render(request, 'roles/asignar_funcion_rol.html', {'rol': rol, 'funciones': funciones})

def asignar_rol_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    roles = Rol.objects.all()
    
    if request.method == 'POST':
        rol_id = request.POST.get('rol')
        rol = get_object_or_404(Rol, id=rol_id)
        UsuarioRol.objects.create(usuario=usuario, rol=rol)
        messages.success(request, 'Rol asignado exitosamente.')
        return redirect('lista_usuarios')
    
    return render(request, 'usuarios/asignar_rol_usuario.html', {'usuario': usuario, 'roles': roles})

# Listar Usuarios con Permisos
def lista_usuarios(request):
    usuarios_con_permisos = Usuario.objects.all()
    usuarios_con_permisos = []

    for usuarios_con_permisos in usuarios_con_permisos:
        permisos = Funcion.objects.filter(rolfuncion__rol__usuariorol__usuario=usuarios_con_permisos)
        usuarios_con_permisos.append({
            'usuario': usuarios_con_permisos,
            'permisos': permisos
        })

        # Imprimir en la consola la información del usuario y sus permisos
        print(f"Usuario: {usuarios_con_permisos.nombre} ({usuarios_con_permisos.user}) - Permisos:")
        for permiso in permisos:
            print(f"  - {permiso.descripcion}")
    
    return render(request, 'log/usuarios/lista_usuarios.html', {'usuarios_con_permisos': usuarios_con_permisos})
