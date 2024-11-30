# Generated by Django 4.2 on 2024-11-30 05:25

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
            name='Retos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reto', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=400)),
                ('puntos', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Retosrespuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagenusuario', models.ImageField(upload_to='pruebas_imagen')),
                ('descripcion', models.TextField(max_length=1000)),
                ('fecha_subida', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('PENDIENTE', 'PENDIENTE'), ('APROVADO', 'APROVADO'), ('RECHAZADO', 'RECHAZADO')], default='PENDIENTE', max_length=50)),
                ('reto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retoshuellascarbono.retos')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rankings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntostotales', models.IntegerField(default=0)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Poemas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulopoema', models.CharField(max_length=90)),
                ('rima', models.TextField(max_length=1000)),
                ('puntospoemas', models.IntegerField(default=0, null=True)),
                ('fecha_subida', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dibujos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombredibujo', models.CharField(max_length=90)),
                ('imagen', models.ImageField(upload_to='dibujos_imagenes')),
                ('puntosdibujo', models.IntegerField(default=0, null=True)),
                ('fecha_subida', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
