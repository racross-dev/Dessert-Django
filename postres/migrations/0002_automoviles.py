# Generated by Django 4.2.1 on 2023-05-15 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postres', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Automoviles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=20)),
                ('placa', models.CharField(max_length=7)),
                ('chofer', models.CharField(max_length=50)),
                ('fecha_adquisicion', models.DateField()),
            ],
        ),
    ]
