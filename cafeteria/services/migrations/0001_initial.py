# Generated by Django 3.2.7 on 2021-09-09 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200, verbose_name='Titulo')),
                ('Subtitle', models.CharField(max_length=200, verbose_name='Subtitulo')),
                ('Content', models.TextField(verbose_name='Contenido')),
                ('Image', models.ImageField(upload_to='media')),
                ('Created', models.TimeField(auto_now_add=True)),
                ('Updated', models.TimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
            },
        ),
    ]
