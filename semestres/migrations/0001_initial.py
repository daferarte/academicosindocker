# Generated by Django 4.1 on 2022-09-23 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nombres del Estudiante')),
                ('Apellido', models.CharField(blank=True, max_length=150, null=True, verbose_name='Apellidos del Estudiante')),
                ('cedula', models.CharField(blank=True, max_length=150, null=True, verbose_name='Cedula')),
                ('celular', models.CharField(blank=True, max_length=100, null=True, verbose_name='Celular')),
                ('carrera', models.CharField(blank=True, max_length=100, null=True, verbose_name='Carrera')),
                ('facultad', models.CharField(blank=True, max_length=100, null=True, verbose_name='Facultad')),
                ('FechaIni', models.CharField(blank=True, max_length=100, null=True, verbose_name='Fecha de Inicio')),
                ('FechaFin', models.CharField(blank=True, max_length=100, null=True, verbose_name='Fecha Fin')),
            ],
            options={
                'verbose_name': 'Semestre',
                'verbose_name_plural': 'Semestres',
            },
        ),
        migrations.CreateModel(
            name='Semestres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=150, verbose_name='Cedula')),
                ('image', models.ImageField(default='null', upload_to='users', verbose_name='Imagen')),
                ('public', models.BooleanField(verbose_name='¿Publicado?')),
                ('fNacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de cumpleaños')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Editado')),
                ('tipoDocumento', models.ManyToManyField(blank=True, to='semestres.semestre', verbose_name='Tipo de documento')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Semestres',
                'verbose_name_plural': 'Semestre',
            },
        ),
    ]
