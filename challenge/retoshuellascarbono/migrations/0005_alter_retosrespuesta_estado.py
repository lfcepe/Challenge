# Generated by Django 4.2 on 2024-12-01 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retoshuellascarbono', '0004_alter_retosrespuesta_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retosrespuesta',
            name='estado',
            field=models.CharField(choices=[('PENDIENTE', 'PENDIENTE'), ('RECHAZADO', 'RECHAZADO'), ('APROBADO', 'APROBADO')], default='PENDIENTE', max_length=50),
        ),
    ]
