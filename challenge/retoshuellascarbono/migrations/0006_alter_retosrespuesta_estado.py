# Generated by Django 4.2 on 2024-11-30 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retoshuellascarbono', '0005_alter_retosrespuesta_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retosrespuesta',
            name='estado',
            field=models.CharField(choices=[('APROVADO', 'APROVADO'), ('PENDIENTE', 'PENDIENTE'), ('RECHAZADO', 'RECHAZADO')], default='PENDIENTE', max_length=50),
        ),
    ]
