# Generated by Django 5.1.1 on 2024-11-06 01:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcion',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='RolFuncion',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('funcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.funcion')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.rol')),
            ],
            options={
                'unique_together': {('rol', 'funcion')},
            },
        ),
        migrations.AddField(
            model_name='rol',
            name='funciones',
            field=models.ManyToManyField(related_name='roles', through='log.RolFuncion', to='log.funcion'),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('nombre', models.CharField(max_length=45)),
                ('user', models.CharField(max_length=45, unique=True)),
                ('pass_field', models.CharField(max_length=45)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='custom_user_groups', related_query_name='custom_user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='custom_user_permissions', related_query_name='custom_user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UsuarioRol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.rol')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.usuario')),
            ],
            options={
                'unique_together': {('usuario', 'rol')},
            },
        ),
        migrations.AddField(
            model_name='usuario',
            name='roles',
            field=models.ManyToManyField(related_name='usuarios_roles', through='log.UsuarioRol', to='log.rol'),
        ),
    ]
