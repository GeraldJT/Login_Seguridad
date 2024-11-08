from django.db import models
from django.contrib.auth.hashers import make_password, check_password


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
    password = models.CharField(max_length=128)  # Aumenta el tamaño para almacenar el hash

    class Meta:
        db_table = 'Usuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.nombre

    # Sobreescribe el método `save` para encriptar la contraseña antes de guardarla
    def save(self, *args, **kwargs):
        # Encripta la contraseña solo si no está encriptada ya
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    # Método para verificar la contraseña
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)


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
