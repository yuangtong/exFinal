# Generated by Django 5.0.3 on 2024-04-05 01:06

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='datosUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nroCelular', models.CharField(blank=True, max_length=16, null=True)),
                ('profesionUsuario', models.CharField(blank=True, max_length=64, null=True)),
                ('perfilUsuario', models.CharField(blank=True, max_length=512, null=True)),
                ('fechaCreacion', models.DateField(default=datetime.date.today)),
                ('userRel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='tareasSistem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTarea', models.CharField(blank=True, max_length=32, null=True)),
                ('descripcionTarea', models.CharField(blank=True, max_length=512, null=True)),
                ('fechaFin', models.DateField(default=datetime.date.today)),
                ('fechaInicio', models.DateField(default=datetime.date.today)),
                ('estadoTarea', models.CharField(blank=True, max_length=16, null=True)),
                ('usuarioCreador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('usuarioResponsable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app4.datosusuario')),
            ],
        ),
    ]
