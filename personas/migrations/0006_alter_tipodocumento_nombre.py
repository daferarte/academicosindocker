# Generated by Django 4.1 on 2022-08-13 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0005_alter_tipodocumento_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipodocumento',
            name='nombre',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Nombre'),
        ),
    ]
