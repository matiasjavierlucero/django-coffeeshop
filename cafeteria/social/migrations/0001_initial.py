# Generated by Django 3.2.7 on 2021-09-09 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.SlugField(max_length=100, unique=True, verbose_name='Nombre Clave')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Url')),
                ('created', models.TimeField(auto_now_add=True)),
                ('updated', models.TimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Redes',
                'ordering': ('name',),
            },
        ),
    ]
