# Generated by Django 3.0.8 on 2020-07-27 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('salas', '0001_initial'),
        ('discentes', '0001_initial'),
        ('cadeiras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateTimeField(auto_now_add=True)),
                ('discente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discentes.Discente')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadeiras.Cadeira')),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salas.Sala')),
            ],
        ),
    ]
