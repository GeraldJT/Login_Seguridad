from django.contrib import admin
from .models import Usuario, Rol, Funcion, RolFuncion, UsuarioRol

# Inline para mostrar la relación de Rol y Funcion en el admin
class RolFuncionInline(admin.TabularInline):
    model = RolFuncion
    extra = 1
    verbose_name = "Función asignada"
    verbose_name_plural = "Funciones asignadas"


# Admin personalizado para Rol, incluyendo sus funciones
@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    inlines = [RolFuncionInline]


# Inline para mostrar la relación de Usuario y Rol en el admin
class UsuarioRolInline(admin.TabularInline):
    model = UsuarioRol
    extra = 1
    verbose_name = "Rol asignado"
    verbose_name_plural = "Roles asignados"


# Admin personalizado para Usuario, incluyendo sus roles
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'user')
    inlines = [UsuarioRolInline]


# Admin personalizado para Funcion
@admin.register(Funcion)
class FuncionAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    search_fields = ('descripcion',)


# Admin personalizado para la tabla intermedia RolFuncion
@admin.register(RolFuncion)
class RolFuncionAdmin(admin.ModelAdmin):
    list_display = ('id', 'funcion', 'rol')
    list_filter = ('rol', 'funcion')


# Admin personalizado para la tabla intermedia UsuarioRol
@admin.register(UsuarioRol)
class UsuarioRolAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'rol')
    list_filter = ('rol', 'usuario')
