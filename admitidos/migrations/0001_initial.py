# Generated by Django 4.1.1 on 2022-09-23 08:59

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
            name='Admitir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellidos', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nombre')),
                ('nombres', models.CharField(blank=True, max_length=100, null=True, verbose_name='Descripcion')),
                ('cedula', models.CharField(blank=True, max_length=20, null=True, verbose_name='Cedula')),
                ('celular', models.CharField(blank=True, max_length=10, null=True, verbose_name='Celular')),
                ('facultad', models.CharField(blank=True, max_length=100, null=True, verbose_name='Facultad')),
                ('carrera', models.CharField(blank=True, max_length=100, null=True, verbose_name='Carrera')),
                ('pasoalsemestre', models.CharField(blank=True, max_length=10, null=True, verbose_name='Semestre Pasado')),
            ],
            options={
                'verbose_name': 'Admitir',
                'verbose_name_plural': 'Admitidos',
            },
        ),
        migrations.CreateModel(
            name='Admitido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='null', upload_to='users', verbose_name='Fotografia')),
                ('public', models.BooleanField(verbose_name='¿Enviar Formulario?')),
                ('admitido', models.BooleanField(verbose_name='¿Si/No?')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Editado')),
                ('principal', models.ManyToManyField(blank=True, to='admitidos.admitir', verbose_name='Principal')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Admitido',
                'verbose_name_plural': 'Admitidos',
            },
        ),
    ]
