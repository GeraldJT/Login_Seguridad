# Generated by Django 5.1.1 on 2024-11-06 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_alter_funcion_options_alter_rol_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rol',
            name='funciones',
            field=models.ManyToManyField(related_name='roles', through='log.RolFuncion', to='log.funcion'),
        ),
    ]
