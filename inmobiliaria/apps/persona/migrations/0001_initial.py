# Generated by Django 3.1.2 on 2020-10-23 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('cod_persona', models.DecimalField(decimal_places=65535, max_digits=65535, primary_key=True, serialize=False)),
                ('cuit_persona', models.CharField(blank=True, max_length=11, null=True)),
                ('tipo_persona', models.CharField(blank=True, max_length=1, null=True)),
                ('nombre_persona', models.CharField(blank=True, max_length=70, null=True)),
                ('mail_persona', models.CharField(blank=True, max_length=50, null=True)),
                ('dom_cod_localidad', models.IntegerField(blank=True, null=True)),
                ('dom_cod_calle', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'persona',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PropietarioPropiedad',
            fields=[
                ('cod_propiedad', models.IntegerField(primary_key=True, serialize=False)),
                ('cod_persona', models.IntegerField()),
                ('fecha_alta', models.DateField(blank=True, null=True)),
                ('escritura_propiedad', models.CharField(blank=True, max_length=2, null=True)),
                ('autorizacion_poder', models.CharField(blank=True, max_length=2, null=True)),
            ],
            options={
                'db_table': 'propietario_propiedad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TelefonoPersona',
            fields=[
                ('cod_persona', models.IntegerField(primary_key=True, serialize=False)),
                ('telefono_persona', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'telefono_persona',
                'managed': False,
            },
        ),
    ]
