# Generated by Django 2.2.3 on 2022-01-22 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Academica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('creditos', models.PositiveSmallIntegerField()),
                ('docente', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fechaMatricula', models.DateTimeField(auto_now_add=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academica.Curso')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academica.Estudiante')),
            ],
        ),
    ]
