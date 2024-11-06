from django.db import models

class Funcion(models.Model):
    id = models.AutoField(primary_key=True, db_column='idFunciones')
    descripcion = models.CharField(max_length=45)

    class Meta:
        db_table = 'Funciones'
        verbose_name = 'Función'
        verbose_name_plural = 'Funciones'

    def __str__(self):
        return self.descripcion


class Rol(models.Model):
    id = models.AutoField(primary_key=True, db_column='idRoles')
    descripcion = models.CharField(max_length=45)
    funciones = models.ManyToManyField(Funcion, through='RolFuncion', related_name='roles')

    class Meta:
        db_table = 'Roles'
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.descripcion


class Usuario(models.Model):
    id = models.AutoField(primary_key=True, db_column='idUsuarios')
    nombre = models.CharField(max_length=45)
    user = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=45)

    class Meta:
        db_table = 'Usuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.nombre


class RolFuncion(models.Model):
    id = models.AutoField(primary_key=True, db_column='idRolesFunciones')
    funcion = models.ForeignKey(Funcion, on_delete=models.CASCADE, db_column='Funciones_idFunciones')
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, db_column='Roles_idRoles')

    class Meta:
        db_table = 'RolesFunciones'
        verbose_name = 'Rol-Función'
        verbose_name_plural = 'Roles-Funciones'
        indexes = [
            models.Index(fields=['funcion'], name='rf_funcion_idx'),
            models.Index(fields=['rol'], name='rf_rol_idx'),
        ]


class UsuarioRol(models.Model):
    id = models.AutoField(primary_key=True, db_column='idUsuariosRoles')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='Usuarios_idUsuarios')
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, db_column='Roles_idRoles')

    class Meta:
        db_table = 'UsuariosRoles'
        verbose_name = 'Usuario-Rol'
        verbose_name_plural = 'Usuarios-Roles'
        indexes = [
            models.Index(fields=['usuario'], name='ur_usuario_idx'),
            models.Index(fields=['rol'], name='ur_rol_idx'),
        ]
