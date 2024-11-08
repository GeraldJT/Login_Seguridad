import random
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Funcion, Rol, Usuario, RolFuncion, UsuarioRol
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            # Intenta obtener el usuario de tu modelo personalizado
            user = Usuario.objects.get(user=username)
            
            # Verifica la contraseña encriptada con `check_password`
            if check_password(password, user.password):
                # Si la contraseña es correcta, se guarda en la sesión
                request.session['user_id'] = user.id
                messages.success(request, f"Bienvenido {user.nombre}")
                return redirect('/admin/log/usuario/')  # Redirige a la página de inicio después del login
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')
        except Usuario.DoesNotExist:
            messages.error(request, 'Usuario o contraseña incorrectos')

    return render(request, 'login.html')


# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UsuarioForm





def logout_view(request):
    logout(request)
    return redirect('login')

# Listar Funciones
def dashboard(request):
    return render (request, 'dashboard.html')

def lista_funciones(request):
    if 'user_id' not in request.session:
        return redirect('login')
    funciones = Funcion.objects.all()
    return render(request, 'log/funciones/lista_funciones.html', {'funciones': funciones})

# Crear Funcion
def crear_funcion(request):
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        Funcion.objects.create(descripcion=descripcion)
        messages.success(request, 'Función creada exitosamente.')
        return redirect('lista_funciones')
    return render(request, 'log/funciones/crear_funcion.html')

# Editar Funcion
def editar_funcion(request, funcion_id):
    funcion = get_object_or_404(Funcion, id=funcion_id)
    if request.method == 'POST':
        funcion.descripcion = request.POST.get('descripcion')
        funcion.save()
        messages.success(request, 'Función actualizada correctamente.')
        return redirect('lista_funciones')
    return render(request, 'log/funciones/editar_funcion.html', {'funcion': funcion})

# Eliminar Funcion
def eliminar_funcion(request, funcion_id):
    funcion = get_object_or_404(Funcion, id=funcion_id)
    funcion.delete()
    messages.success(request, 'Función eliminada correctamente.')
    return redirect('lista_funciones')

# Listar Roles
def lista_roles(request):
    roles = Rol.objects.all()
    return render(request, 'log/roles/lista_roles.html', {'roles': roles})

# Crear Rol
def crear_rol(request):
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        Rol.objects.create(descripcion=descripcion)
        messages.success(request, 'Rol creado exitosamente.')
        return redirect('lista_roles')
    return render(request, 'log/roles/crear_rol.html')

# Editar Rol
def editar_rol(request, rol_id):
    rol = get_object_or_404(Rol, id=rol_id)
    if request.method == 'POST':
        rol.descripcion = request.POST.get('descripcion')
        rol.save()
        messages.success(request, 'Rol actualizado correctamente.')
        return redirect('lista_roles')
    return render(request, 'log/roles/editar_funcion_rol.html', {'rol': rol})

# Eliminar Rol
def eliminar_rol(request, rol_id):
    rol = get_object_or_404(Rol, id=rol_id)
    rol.delete()
    messages.success(request, 'Rol eliminado correctamente.')
    return redirect('lista_roles')

# Listar Usuarios
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
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
    
    return render(request, 'log/usuarios/editar_usuario.html', {'usuario': usuario})

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
    
    return render(request, 'log/roles/asignar_funcion_rol.html', {'rol': rol, 'funciones': funciones})

def asignar_rol_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    roles = Rol.objects.all()
    
    if request.method == 'POST':
        rol_id = request.POST.get('rol')
        rol = get_object_or_404(Rol, id=rol_id)
        UsuarioRol.objects.create(usuario=usuario, rol=rol)
        messages.success(request, 'Rol asignado exitosamente.')
        return redirect('lista_usuarios')
    
    return render(request, 'log/usuarios/asignar_rol_usuario.html', {'usuario': usuario, 'roles': roles})

# Listar Usuarios con Permisos
def lista_usuarios(request):    
    usuarios_con_permisos = []

    # Itera sobre cada usuario y obtén sus permisos
    for usuario in Usuario.objects.all():
        permisos = Funcion.objects.filter(roles__usuariorol__usuario=usuario)
        usuarios_con_permisos.append({
            'usuario': usuario,
            'permisos': permisos
        })

        # Imprimir en la consola la información del usuario y sus permisos
        print(f"Usuario: {usuario.nombre} ({usuario.user}) - Permisos:")
        for permiso in permisos:
            print(f"  - {permiso.descripcion}")

    return render(request, 'log/usuarios/lista_usuarios.html', {'usuarios_con_permisos': usuarios_con_permisos})


from django.core.mail import send_mail
from django.conf import settings

def generar_codigo_verificacion():
    """Genera un código de verificación aleatorio de 6 dígitos."""
    return random.randint(100000, 999999)

def enviar_codigo_verificacion(email, codigo):
    """Envía el código de verificación al correo del usuario."""
    subject = 'Código de verificación de registro'
    message = f'Este es tu código de verificación: {codigo}'
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])

def registro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            # Guardar el nuevo usuario sin la contraseña encriptada
            usuario = form.save(commit=False)
            usuario.password = usuario.password  # Guarda la contraseña sin encriptar aún
            usuario.save()

            # Generar y enviar el código de verificación
            codigo = generar_codigo_verificacion()
            enviar_codigo_verificacion(usuario.email, codigo)
            
            # Puedes guardar el código en el usuario o en un modelo de verificación separado
            request.session['codigo_verificacion'] = codigo  # Guardamos el código en la sesión
            request.session['usuario_id'] = usuario.id  # Guardamos el ID del usuario

            messages.success(request, 'Registro exitoso. Te hemos enviado un código de verificación a tu correo.')
            return redirect('verificar_codigo')  # Redirigir a una vista para verificar el código
        else:
            messages.error(request, 'Por favor, revisa los errores en el formulario.')
    else:
        form = UsuarioForm()

    return render(request, 'registro.html', {'form': form})



def verificar_codigo(request):
    if request.method == 'POST':
        codigo_ingresado = request.POST.get('codigo')
        codigo_guardado = request.session.get('codigo_verificacion')

        if str(codigo_ingresado) == str(codigo_guardado):
            # Si el código es correcto, activar el usuario
            usuario_id = request.session.get('usuario_id')
            usuario = Usuario.objects.get(id=usuario_id)
            usuario.is_active = True  # O cualquier otra lógica para marcar el usuario como verificado
            usuario.save()

            messages.success(request, 'Cuenta verificada correctamente. Ahora puedes iniciar sesión.')
            return redirect('login')  # Redirige a la página de login
        else:
            messages.error(request, 'Código incorrecto. Intenta nuevamente.')

    return render(request, 'verificar_codigo.html')
