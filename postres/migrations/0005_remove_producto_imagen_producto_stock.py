# Generated by Django 4.2.1 on 2023-05-15 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postres', '0004_producto_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='imagen',
        ),
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
