# Generated by Django 4.1 on 2022-08-13 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0004_tipodocumento_create_at_tipodocumento_update_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipodocumento',
            name='nombre',
            field=models.CharField(max_length=150, verbose_name='Nombre'),
        ),
    ]