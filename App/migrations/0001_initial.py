# Generated by Django 4.0.3 on 2022-04-10 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('entregables', models.CharField(max_length=10)),
                ('FechaDeInicio', models.DateField()),
                ('FechaDeFin', models.DateField()),
                ('Horario', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Entregables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=20)),
                ('FechaEntrega', models.DateField()),
                ('Nota', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
                ('apellido', models.CharField(max_length=20)),
                ('curso', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profesores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
                ('apellido', models.CharField(max_length=20)),
                ('curso', models.CharField(max_length=20)),
            ],
        ),
    ]
